import pandas as pd
import os

input_file=os.path.join("data","raw","02_nav_history.csv")

df=pd.read_csv(input_file)

print(df.head())

print(df.shape)
print(df.dtypes)

df["date"] = pd.to_datetime(df["date"])

print(df["date"].head(10))
print(df["date"].dtype)


df=df.sort_values(by=["amfi_code","date"])
print(df[["amfi_code","date"]].head(15))

print(df["nav"].isnull().sum())

df["nav"]= df.groupby("amfi_code")["nav"].ffill()
print(df["nav"].isnull().sum())

print(df.duplicated().sum())

invalid_nav = df[df["nav"] <= 0]
print(len(invalid_nav))

os.makedirs("data/processes", exist_ok=True)
output_file = os.path.join("data", "processed", "02_nav_history_cleaned.csv")
df.to_csv(output_file, index=False)
print("\nCleaned file saved successfully!")



# ============================================================================================================

input_file = os.path.join("data", "raw", "08_investor_transactions.csv")

df = pd.read_csv(input_file)
print(df.head())
print(df.dtypes)
print(df.shape)

print(df["transaction_type"].unique())

print((df["amount_inr"] <= 0).sum())
df["transaction_date"] = pd.to_datetime(df["transaction_date"])
print(df["transaction_date"].dtype)

print(df["kyc_status"].unique())

output_file = os.path.join("data","processed","08_investor_transactions_cleaned.csv")
df.to_csv(output_file, index=False)

print("Investor Transactions cleaned and saved!")


# ===================================================================================================


# =====================================
# Task 3: Clean scheme_performance.csv
# =====================================

input_file = os.path.join("data", "raw", "07_scheme_performance.csv")

df = pd.read_csv(input_file)

print(df.head())
print(df.dtypes)
print(df.shape)

print(df.columns)

print(df[["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]].dtypes)

df["return_1yr_pct"] = pd.to_numeric(df["return_1yr_pct"], errors="coerce")
df["return_3yr_pct"] = pd.to_numeric(df["return_3yr_pct"], errors="coerce")
df["return_5yr_pct"] = pd.to_numeric(df["return_5yr_pct"], errors="coerce")

print("1 Year :", df["return_1yr_pct"].isna().sum())
print("3 Year :", df["return_3yr_pct"].isna().sum())
print("5 Year :", df["return_5yr_pct"].isna().sum())

invalid_expense = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]
print(len(invalid_expense))

output_file = os.path.join("data","processed","07_scheme_performance_cleaned.csv"
)
df.to_csv(output_file, index=False)
print("Scheme Performance cleaned and saved!")