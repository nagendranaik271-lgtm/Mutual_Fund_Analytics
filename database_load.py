import pandas as pd
from sqlalchemy import create_engine
import os

engine = create_engine("sqlite:///bluestock_mf.db")

file_path = os.path.join("data","processed","02_nav_history_cleaned.csv")
df = pd.read_csv(file_path)

df.to_sql("fact_nav",engine,if_exists="replace",index=False)
print("NAV table loaded successfully!")


file_path = os.path.join("data","processed","02_nav_history_cleaned.csv")
df = pd.read_csv(file_path)
df.to_sql("fact_nav",engine,if_exists="replace",index=False)
print("fact_nav table loaded!")
print(df.shape)

file_path=os.path.join("data","processed","08_investor_transactions_cleaned.csv")
df=pd.read_csv(file_path)
df.to_sql("fact_transactions",engine,if_exists="replace",index=False)
print("fact_tansactions table loaded")
print(df.shape)

file_path=os.path.join("data","processed","07_scheme_performance_cleaned.csv")
df=pd.read_csv(file_path)
df.to_sql("fact_performance",engine,if_exists="replace",index=False)
print("fact_performance table loaded!")
print(df.shape)

file_path = os.path.join("data","raw","01_fund_master.csv")
df = pd.read_csv(file_path)
df.to_sql("dim_fund",engine,if_exists="replace",index=False)
print("dim_fund table loaded!")
print(df.shape)

