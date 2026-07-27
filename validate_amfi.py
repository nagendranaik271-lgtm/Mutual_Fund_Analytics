import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

print(len(fund_codes))
print(len(nav_codes))

missing_codes = fund_codes - nav_codes
print("missing_codes:")
print(missing_codes)

print("\nData Quality Summary")
print("-" * 30)
print(f"Total AMFI Codes in Fund Master : {len(fund_codes)}")
print(f"Total AMFI Codes in NAV History : {len(nav_codes)}")
print(f"Missing AMFI Codes              : {len(missing_codes)}")

if len(missing_codes) == 0:
    print("\n All AMFI codes in fund_master exist in nav_history.")
    print(" Data Quality Check Passed.")
else:
    print("\n Some AMFI codes are missing.")
    print(missing_codes)
