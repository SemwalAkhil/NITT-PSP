# 6. Write a program to serialize student marks dictionary to a binary file using pickle and calculate percentages.
# Input: (marks.dat 3 1 "60 80 30 70" 2 "90 60 50 40" 3 "10 50 30 40"), (m.dat 1 101 "75 85")
# Output:
#   Run 1:
#   Student Percentages:
#   Roll 1: 60.00%
#   Roll 2: 60.00%
#   Roll 3: 32.50%
#   Run 2:
#   Student Percentages:
#   Roll 101: 80.00%

import pickle

filename = input("Enter binary filename: ")
n = int(input("Enter number of students: "))
marks = {}
for i in range(n):
    roll = int(input("Enter roll number: "))
    m_list = [int(x) for x in input(f"Enter marks for roll {roll}: ").split()]
    marks[roll] = m_list

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
