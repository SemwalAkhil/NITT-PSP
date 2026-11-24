# 17. Write a program to inspect and summarize student dataset using pandas.
# Input: None (data defined in the script)
# Output:
#   Shape: (4464, 13)
#   Average CGPA: 3.41
#   Average Age: 22.62

import os
import pandas as pd

csv_path = os.path.join(os.path.dirname(__file__), "Student_Depression_Dataset.csv")
df = pd.read_csv(csv_path, encoding="utf-8-sig")

print("Shape:", df.shape)
print("Columns:", list(df.columns[:5]))
print("Average CGPA:", round(df["CGPA"].mean(), 2))
print("Average Age:", round(df["Age"].mean(), 2))
print("Depression counts:")
print(df["Depression"].value_counts())
print("Gender breakdown:")
print(df["Gender"].value_counts())
