import pandas as pd
import os

raw_folder = "data/raw"
processed_folder = "data/processed"

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

    print("\n" + "=" * 60)
    print("Dataset:", file)

    file_path = os.path.join(raw_folder, file)

    df = pd.read_csv(file_path)

    print("Shape:", df.shape)

    print("Missing Values:")
    print(df.isnull().sum())

    print("Duplicate Rows:", df.duplicated().sum())

    if file == "04_monthly_sip_inflows.csv":
        print(df[df["yoy_growth_pct"].isnull()])

     # YoY growth for 2022 is intentionally NaN because there is no 2021 data available for comparison.

    output_path = os.path.join(processed_folder, file)
    df.to_csv(output_path, index=False)

    print(f"{file} saved to processed folder.")