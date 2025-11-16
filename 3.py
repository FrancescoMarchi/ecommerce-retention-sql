import re
import pandas as pd
import numpy as np

# Read with flexible delimiter; keep everything as string first
df = pd.read_csv("orders.csv", engine="python", sep=None, dtype=str)
df.columns = [c.strip().lower() for c in df.columns]

# Standardize header names
rename_map = {
    "order_id": "order_id",
    "order id": "order_id",
    "customer_id": "customer_id",
    "customer id": "customer_id",
    "order_date": "order_date",
    "order date": "order_date",
    "order_value": "order_value",
    "order value": "order_value",
}
df = df.rename(columns=rename_map)

# Keep required columns & strip whitespace
df = df[["order_id", "customer_id", "order_date", "order_value"]].copy()
for c in ["order_id", "customer_id"]:
    df[c] = df[c].astype(str).str.strip()

# Normalize dates → YYYY-MM-DD
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce").dt.strftime("%Y-%m-%d")

# Clean order_value text: remove currency, spaces, thousand separators, handle decimal comma & (negatives)
def to_float_safe(x: str):
    if pd.isna(x):
        return np.nan
    s = str(x).strip()

    # Handle parentheses for negative amounts: (123.45) -> -123.45
    neg = False
    if s.startswith("(") and s.endswith(")"):
        neg = True
        s = s[1:-1]

    # Remove currency symbols and spaces
    s = re.sub(r"[^\d,\.\-]", "", s)

    # If there are both comma and dot, assume comma is thousand sep -> remove commas
    if "," in s and "." in s:
        s = s.replace(",", "")
    # If only comma, treat it as decimal comma
    elif "," in s and "." not in s:
        s = s.replace(",", ".")

    try:
        v = float(s)
        return -v if neg else v
    except:
        return np.nan

df["order_value"] = df["order_value"].apply(to_float_safe)

# Drop rows with missing critical fields or invalid conversions
df = df.dropna(subset=["order_id", "customer_id", "order_date", "order_value"])

# Round to 2 decimals (optional)
df["order_value"] = df["order_value"].round(2)

# Write a clean CSV with exact schema and comma delimiter
df.to_csv("orders_clean.csv", index=False)
print("Wrote orders_clean.csv with", len(df), "rows")
