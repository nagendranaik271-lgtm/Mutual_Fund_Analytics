from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def inspect_dataset(file_path: Path) -> None:
    """Inspect a CSV dataset and display basic metadata."""
    try:
        df = pd.read_csv(file_path)

        print(f"Dataset: {file_path.name}")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")
        print()

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")

    except Exception as exc:
        print(f"Error reading {file_path.name}: {exc}")


def inspect_fund_master(file_path: Path) -> None:
    """Display unique fund-master classifications."""
    try:
        df = pd.read_csv(file_path)

        print("Unique Fund Houses:")
        print(df["fund_house"].dropna().unique())

        print("\nUnique Categories:")
        print(df["category"].dropna().unique())

        print("\nUnique Sub Categories:")
        print(df["sub_category"].dropna().unique())

        print("\nUnique Risk Categories:")
        print(df["risk_category"].dropna().unique())

    except KeyError as exc:
        print(f"Missing expected column: {exc}")

    except Exception as exc:
        print(f"Error inspecting fund master: {exc}")


def main() -> None:
    """Inspect all raw CSV datasets."""
    if not RAW_DATA_DIR.exists():
        raise FileNotFoundError(
            f"Raw data directory not found: {RAW_DATA_DIR}"
        )

    csv_files = sorted(RAW_DATA_DIR.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in the raw data directory.")
        return

    print(f"CSV files found: {len(csv_files)}\n")

    for file_path in csv_files:
        print("=" * 60)
        inspect_dataset(file_path)

        if file_path.name == "01_fund_master.csv":
            inspect_fund_master(file_path)

        print()


if __name__ == "__main__":
    main()