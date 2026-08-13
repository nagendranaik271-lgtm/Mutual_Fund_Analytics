import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine("sqlite:///bluestock_mf.db")


# ============================================================
# 1. Load NAV history
# ============================================================

file_path = os.path.join(
    "data", "processed", "02_nav_history_cleaned.csv"
)

df = pd.read_csv(file_path)

df.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav table loaded!")
print(df.shape)


# ============================================================
# 2. Load investor transactions
# ============================================================

file_path = os.path.join(
    "data", "processed", "08_investor_transactions_cleaned.csv"
)

df = pd.read_csv(file_path)

df.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions table loaded!")
print(df.shape)


# ============================================================
# 3. Load scheme performance
# ============================================================

file_path = os.path.join(
    "data", "processed", "07_scheme_performance_cleaned.csv"
)

df = pd.read_csv(file_path)

df.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance table loaded!")
print(df.shape)


# ============================================================
# 4. Load fund master
# ============================================================

file_path = os.path.join(
    "data", "raw", "01_fund_master.csv"
)

df = pd.read_csv(file_path)

df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund table loaded!")
print(df.shape)


# ============================================================
# 5. Load AUM
# ============================================================

file_path = os.path.join(
    "data", "processed", "03_aum_by_fund_house.csv"
)

df = pd.read_csv(file_path)

df.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("fact_aum table loaded!")
print(df.shape)


# ============================================================
# 6. Load monthly SIP inflows
# ============================================================

file_path = os.path.join(
    "data", "processed", "04_monthly_sip_inflows.csv"
)

df = pd.read_csv(file_path)

df.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

print("monthly_sip_inflows table loaded!")
print(df.shape)


print("\nDatabase loading completed successfully!")
