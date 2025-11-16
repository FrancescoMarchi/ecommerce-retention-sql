# generate_biased_data.py
import numpy as np, pandas as pd

rng = np.random.default_rng(42)  # reproducible

# ---- If you already have customers.csv with IDs, signup_date, location, it will reuse it ----
N = 4957
try:
    base = pd.read_csv("customers.csv")
    assert {"customer_id","signup_date","location"}.issubset(base.columns)
    customers = base[["customer_id","signup_date","location"]].copy()
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])
except Exception:
    customers = pd.DataFrame({
        "customer_id": [f"C{str(i).zfill(5)}" for i in range(1, N+1)],
        "signup_date": rng.choice(pd.date_range("2023-01-01","2025-09-30",freq="D"), size=N),
        "location": rng.choice(["hcmc","hanoi","taipei","danang"], size=N, p=[0.55,0.20,0.15,0.10]),
    })

# ---- Channel assignment (biased mix) ----
channels = ["email","paid_search","social","referral","organic"]
p_mix    = [0.15,   0.30,         0.25,    0.10,      0.20]
customers["channel"] = rng.choice(channels, size=len(customers), p=p_mix)

# ---- Behavioral biases ----
p_ret    = {"email":.70,"paid_search":.45,"social":.60,"referral":.75,"organic":.55}  # returning probability
mu       = {"email":230,"paid_search":210,"social":220,"referral":240,"organic":215}  # AOV mean
sd       = {"email": 60,"paid_search": 70,"social": 65,"referral": 60,"organic": 55}  # AOV sd
p_refund = {"email":.025,"paid_search":.04,"social":.03,"referral":.018,"organic":.022}

# Location & seasonality multipliers
loc_mult = {"hcmc":1.00,"hanoi":1.03,"taipei":1.08,"danang":0.94}
def quarter_mult(dt: pd.Timestamp) -> float:
    q = ((dt.month-1)//3)+1
    return {1:1.02, 2:0.97, 3:0.98, 4:1.08}[q]  # Q4 up, Q2/Q3 slightly down

# ---- Orders per customer (lifetime) ----
is_ret = customers["channel"].map(p_ret).pipe(lambda p: rng.random(len(p)) < p)
orders_per_customer = np.where(is_ret, rng.integers(2, 7, size=len(customers)), 1)  # 2–6 if returning

# ---- Expand to orders with realistic values ----
all_days = pd.date_range("2023-01-01","2025-12-31",freq="D")
rows = []
oid = 1
for cid, ch, loc, n in zip(customers["customer_id"], customers["channel"], customers["location"], orders_per_customer):
    chosen = rng.choice(all_days, size=n, replace=False); chosen.sort()
    for d in chosen:
        base_val = max(5, rng.normal(mu[ch], sd[ch]))
        val = base_val * loc_mult[loc] * quarter_mult(pd.Timestamp(d))
        net = -abs(val) if rng.random() < p_refund[ch] else abs(val)
        rows.append((f"O{oid:07d}", cid, str(pd.Timestamp(d).date()), round(float(net),2)))
        oid += 1

orders = pd.DataFrame(rows, columns=["order_id","customer_id","order_date","order_value"])

# ---- Save CSVs matching BigQuery schemas ----
cust_out = customers[["customer_id","signup_date","channel","location"]].copy()
cust_out["signup_date"] = pd.to_datetime(cust_out["signup_date"]).dt.date
cust_out.to_csv("customers.csv", index=False)
orders.to_csv("orders.csv", index=False)

print("Generated customers.csv:", len(cust_out), "rows")
print("Generated orders.csv:", len(orders), "rows")
