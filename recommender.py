import pandas as pd


# Load fund performance data
file_path = "data/processed/07_scheme_performance_cleaned.csv"

funds = pd.read_csv(file_path)


def recommend_funds(risk_appetite):
    """
    Recommend top 3 funds by Sharpe ratio
    for the selected risk appetite.
    """

    # Standardize input
    risk_appetite = risk_appetite.strip().title()

    valid_risks = ["Low", "Moderate", "High"]

    if risk_appetite not in valid_risks:
        print("Invalid risk appetite.")
        print("Choose: Low, Moderate, or High")
        return

    # Filter by risk grade
    matching_funds = funds[
        funds["risk_grade"].str.strip().str.title()
        == risk_appetite
    ].copy()

    # Sort by Sharpe ratio
    recommendations = (
        matching_funds
        .sort_values("sharpe_ratio", ascending=False)
        .head(3)
    )

    # Select useful columns
    recommendations = recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_1yr_pct",
            "std_dev_ann_pct"
        ]
    ]

    print(f"\nTop 3 Fund Recommendations — {risk_appetite} Risk")
    print("=" * 70)

    print(
        recommendations.to_string(index=False)
    )

    return recommendations


# User input
if __name__ == "__main__":

    risk = input(
        "Enter risk appetite (Low / Moderate / High): "
    )

    recommend_funds(risk)