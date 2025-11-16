import pandas as pd

# Read customers.csv with flexible delimiter and robust date parsing
df = pd.read_csv("customers.csv", engine="python", sep=None, dtype=str)
df.columns = [c.strip().lower() for c in df.columns]

# Map/rename common header variants → exact names BigQuery expects
rename_map = {
    "customer": "customer_id",
    "customer_id": "customer_id",
    "signup_date": "signup_date",
    "channel": "channel",
    "location": "location",
}
df = df.rename(columns=rename_map)

# Keep only required columns in correct order
df = df[["customer_id", "signup_date", "channel", "location"]].copy()

# Trim whitespace
for c in ["customer_id", "channel", "location"]:
    df[c] = df[c].astype(str).str.strip()

# Normalize date to ISO YYYY-MM-DD
df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce").dt.strftime("%Y-%m-%d")

# Drop rows with missing critical fields or invalid date
df = df.dropna(subset=["customer_id", "signup_date", "channel", "location"])

# Write clean file with comma delimiter and proper header
df.to_csv("customers_clean.csv", index=False)
print("Wrote customers_clean.csv with", len(df), "rows")
