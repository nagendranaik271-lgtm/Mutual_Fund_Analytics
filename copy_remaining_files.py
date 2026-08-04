import os
import shutil

source_folder = "data/raw"
destination_folder = "data/processed"

os.makedirs(destination_folder, exist_ok=True)

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    source = os.path.join(source_folder, file)
    destination = os.path.join(destination_folder, file)

    shutil.copy(source, destination)

    print(f"{file} copied successfully!")