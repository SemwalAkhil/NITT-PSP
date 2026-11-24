# 7. Write a program to validate dates in a file line by line using try-except-finally.
# Input: (1), (2)
# Output:
#   Valid date: 15-08-1947
#   Valid date: 26-01-1950
#   Valid date: 29-02-2024
#   Valid date: 10-05-2026
#   Valid date: 31-12-2023
#   Valid date: 01-01-2025
#   Valid date: 15-10-2021
#   Valid date: 30-04-2022
#   File closed successfully in finally block

from datetime import datetime
import os

sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data")
choice = input("Use sample data? (1 = clean, 2 = with errors, 0 = type my own): ").strip()

if choice == "1":
    filename = os.path.join(sample_dir, "dates_clean.txt")
elif choice == "2":
    filename = os.path.join(sample_dir, "dates_errors.txt")
else:
    filename = input("Enter dates filename: ")
    n = int(input("Enter number of dates: "))
    with open(filename, "w") as f:
        for i in range(n):
            f.write(input("Enter date (DD-MM-YYYY): ") + "\n")

f = None
try:
    f = open(filename, "r")
    for line in f:
        d_str = line.strip()
        if not d_str:
            continue
        try:
            valid_date = datetime.strptime(d_str, "%d-%m-%Y")
            print(f"Valid date: {d_str}")
        except ValueError:
            print(f"Invalid date: {d_str}")
except FileNotFoundError:
    print(f"File {filename} not found")
finally:
    if f is not None:
        f.close()
        print("File closed successfully in finally block")
