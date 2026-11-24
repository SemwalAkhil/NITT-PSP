# use kaggle dataset for pandas
import io
import pandas as pd



def main() -> None:
    # 1. Load data (replace io.StringIO(CSV_DATA) with "your_file.csv" for a real file)
    df = pd.read_csv(r"C:\Users\TEMP\Desktop\205126009\Student_Depression_Dataset.csv")

    print("=== 1. Basic Inspection ===")
    print("Shape (rows, cols):", df.shape)
    print("Columns:", list(df.columns))
    print("\nData types:\n", df.dtypes)
    print("\nMissing values per column:\n", df.isna().sum())
    print("\nFirst 3 rows:\n", df.head(3))

    print("\n=== 2. Numerical Summary ===")
    print(df[["Age", "Current_semester", "CGPA", "Cost_without_study"]].describe())

    print("\n=== 3. Filtering & Column Selection ===")
    high_cgpa_depressed = df.loc[
        (df["CGPA"] >= 3.7) & (df["Depression"] == "Yes"),
        ["Gender", "Age", "CGPA", "Living_style", "Cost_without_study"],
    ]
    print("CGPA >= 3.7 and Depression == Yes:\n", high_cgpa_depressed)

    print("\n=== 4. Sorting ===")
    sorted_by_cost = df.sort_values(by="Cost_without_study", ascending=False)
    print(
        "Sorted by Cost_without_study (high to low):\n",
        sorted_by_cost[["Gender", "Living_style", "Home_division", "Cost_without_study"]],
    )

    print("\n=== 5. GroupBy Aggregations ===")
    by_gender = df.groupby("Gender", as_index=False).agg(
        count=("CGPA", "count"),
        avg_cgpa=("CGPA", "mean"),
        avg_cost=("Cost_without_study", "mean"),
        depression_yes=("Depression", lambda s: (s == "Yes").sum()),
    )
    print("Summary by Gender:\n", by_gender.round(2))

    by_living = df.groupby("Living_style", as_index=False).agg(
        count=("Age", "count"),
        avg_cgpa=("CGPA", "mean"),
        avg_cost=("Cost_without_study", "mean"),
    )
    print("\nSummary by Living_style:\n", by_living.round(2))

    print("\n=== 6. Adding Derived Columns ===")
    df["Cost_per_semester"] = (df["Cost_without_study"] / df["Current_semester"]).round(2)
    df["High_CGPA"] = df["CGPA"] >= 3.7
    print(df[["Gender", "Current_semester", "Cost_without_study", "Cost_per_semester", "High_CGPA"]])


if __name__ == "__main__":
    main()