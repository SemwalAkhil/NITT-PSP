# 6. Write a program to serialize student marks dictionary to a binary file using pickle and calculate percentages.
# Input: (1), (2)
# Output:
#   Run 1:
#   Student Percentages:
#   Roll 1: 60.00%
#   Roll 2: 60.00%
#   Roll 3: 32.50%
#   Roll 4: 82.50%
#   Roll 5: 58.75%
#   Run 2:
#   Corrupt pickle file E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\student_marks_corrupt.dat

import pickle
import os

sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data")
choice = input("Use sample data? (1 = clean, 2 = with errors, 0 = type my own): ").strip()

if choice == "1":
    filename = os.path.join(sample_dir, "student_marks_clean.dat")
elif choice == "2":
    filename = os.path.join(sample_dir, "student_marks_corrupt.dat")
else:
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
except (pickle.UnpicklingError, EOFError, ValueError):
    print(f"Corrupt pickle file {filename}")
