# 17. Write a program to inspect and summarize student dataset using pandas.
# Input: NA
# Output:
#   Run 1:
#   Shape: (25, 13)
#   Average CGPA: 3.42
#   Average Age: 22.04
#   Run 2:
#   Shape: (4464, 13)
#   Average CGPA: 3.41
#   Average Age: 22.62

import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "sample_data", "Student_Depression_Dataset_sample.csv")


df = pd.read_csv(csv_path, encoding="utf-8-sig")

print("Shape:", df.shape)
print("Columns:", list(df.columns[:5]))
print("Average CGPA:", round(df["CGPA"].mean(), 2))
print("Average Age:", round(df["Age"].mean(), 2))
print("Depression counts:")
print(df["Depression"].value_counts())
print("Gender breakdown:")
print(df["Gender"].value_counts())
