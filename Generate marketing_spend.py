# data_generation/marketing_spend.py
# Deterministic monthly marketing spend generator (2023-01 to 2025-12)

import csv
from datetime import date
from calendar import monthrange
import random

# -------------------------
# CONFIG (edit as needed)
# -------------------------
CHANNELS = ["email", "paid_search", "referral", "social", "organic"]
BASE_SPEND = {  # average monthly spend per channel (USD)
    "email": 6000,
    "paid_search": 18000,
    "referral": 3500,
    "social": 9000,
    "organic": 0,       # SEO is “free” (can keep 0)
}
MONTHLY_VARIATION = 0.10  # +/-10% random variation
START = (2023, 1)
END   = (2025, 12)
RANDOM_SEED = 42
OUTPUT_CSV = "data/marketing_spend.csv"
# -------------------------

def month_iter(start_y, start_m, end_y, end_m):
    y, m = start_y, start_m
    while (y < end_y) or (y == end_y and m <= end_m):
        yield y, m
        m += 1
        if m > 12:
            m = 1
            y += 1

def first_of_month(y, m):
    return date(y, m, 1)

def main():
    random.seed(RANDOM_SEED)
    rows = []

    for y, m in month_iter(START[0], START[1], END[0], END[1]):
        month_date = first_of_month(y, m).isoformat()  # YYYY-MM-01
        for ch in CHANNELS:
            base = BASE_SPEND[ch]
            if base == 0:
                spend = 0
            else:
                # Apply symmetric variation, clamp to >= 0
                factor = 1 + random.uniform(-MONTHLY_VARIATION, MONTHLY_VARIATION)
                spend = int(round(max(base * factor, 0)))
            rows.append((month_date, ch, spend))

    # Ensure output folder exists
    import os
    os.makedirs(os.path.dirname(OUTPUT_CSV), exist_ok=True)

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["month", "channel", "spend_usd"])
        writer.writerows(rows)

    # Quick sanity summary
    totals = {}
    for _, ch, sp in rows:
        totals[ch] = totals.get(ch, 0) + sp
    print(f"Wrote {len(rows)} rows to {OUTPUT_CSV}")
    for ch in CHANNELS:
        print(f"  {ch:12s} total spend: ${totals.get(ch,0):,}")

if __name__ == "__main__":
    main()
