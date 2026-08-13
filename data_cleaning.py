from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"


def clean_nav():
    """Clean NAV history and save the processed dataset."""
    input_file = RAW_DIR / "02_nav_history.csv"
    output_file = PROCESSED_DIR / "02_nav_history_cleaned.csv"

    df = pd.read_csv(input_file)

    df["date"] = pd.to_datetime(df["date"])
    df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

    df = df.sort_values(["amfi_code", "date"])

    cleaned_groups = []

    for amfi_code, group in df.groupby("amfi_code"):
        group = group.set_index("date")

        full_dates = pd.date_range(
            start=group.index.min(),
            end=group.index.max(),
            freq="D"
        )

        group = group.reindex(full_dates)
        group["amfi_code"] = amfi_code
        group["nav"] = group["nav"].ffill()

        group.index.name = "date"
        group = group.reset_index()

        cleaned_groups.append(group)

    df = pd.concat(cleaned_groups, ignore_index=True)

    df = df[["amfi_code", "date", "nav"]]
    df = df.drop_duplicates()

    df.to_csv(output_file, index=False)

    print(f"NAV cleaned: {len(df):,} rows")


def clean_transactions():
    """Clean investor transactions."""
    input_file = RAW_DIR / "08_investor_transactions.csv"
    output_file = PROCESSED_DIR / "08_investor_transactions_cleaned.csv"

    df = pd.read_csv(input_file)

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"],
        errors="coerce"
    )

    df["amount_inr"] = pd.to_numeric(
        df["amount_inr"],
        errors="coerce"
    )

    df.to_csv(output_file, index=False)

    print(f"Transactions cleaned: {len(df):,} rows")


def clean_performance():
    """Clean scheme performance data."""
    input_file = RAW_DIR / "07_scheme_performance.csv"
    output_file = PROCESSED_DIR / "07_scheme_performance_cleaned.csv"

    df = pd.read_csv(input_file)

    numeric_columns = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "benchmark_3yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "std_dev_ann_pct",
        "max_drawdown_pct",
        "aum_crore",
        "expense_ratio_pct"
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce"
            )

    df.to_csv(output_file, index=False)

    print(f"Performance cleaned: {len(df):,} rows")


def main():
    """Run all data-cleaning tasks."""
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    clean_nav()
    clean_transactions()
    clean_performance()

    print("\nData cleaning completed successfully!")


if __name__ == "__main__":
    main()