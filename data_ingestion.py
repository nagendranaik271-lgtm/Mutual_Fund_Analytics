import os
import pandas as pd

folder_path = "data/raw"

csv_files = [file for file in os.listdir(folder_path) if file.endswith(".csv")]

print("CSV Files Found:")
print(csv_files)

for file in csv_files:

    print("\n" + "=" * 60)
    print("Dataset:", file)

    file_path = os.path.join(folder_path, file)

    df = pd.read_csv(file_path)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    if file == "01_fund_master.csv":

        print("\nUnique Fund Houses:")
        print(df["fund_house"].unique())

        print("\nUnique Categories:")
        print(df["category"].unique())

        print("\nUnique Sub Categories:")
        print(df["sub_category"].unique())

        print("\nUnique Risk Categories:")
        print(df["risk_category"].unique())