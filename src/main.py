import pandas as pd
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    csv_path = project_root / "data" / "sample.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Expected CSV at {csv_path}")

    df = pd.read_csv(csv_path)

    print("=== Head ===")
    print(df.head())

    print("\n=== Describe ===")
    print(df.describe(include="all"))

    print("\n=== Group by 'category' and sum 'value' ===")
    grouped = df.groupby("category", dropna=False)["value"].sum().reset_index()
    print(grouped)


if __name__ == "__main__":
    main()


