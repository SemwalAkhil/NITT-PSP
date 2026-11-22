# 6. Write a program to serialize and deserialize student marks using pickle and compute percentages.
# Input: None (data defined in the script)
# Output:
#   Student Percentages:
#   Roll 1: 60.00%
#   Roll 2: 60.00%
#   Roll 3: 32.50%

import pickle

filename = "marks.dat"
marks = {
    1: [60, 80, 30, 70],
    2: [90, 60, 50, 40],
    3: [10, 50, 30, 40]
}

with open(filename, "wb") as f:
    pickle.dump(marks, f)

try:
    with open(filename, "rb") as f:
        loaded_marks = pickle.load(f)
    print("Student Percentages:")
    for roll, m in loaded_marks.items():
        percentage = sum(m) / len(m)
        print(f"Roll {roll}: {percentage:.2f}%")
except FileNotFoundError:
    print(f"File {filename} not found")
