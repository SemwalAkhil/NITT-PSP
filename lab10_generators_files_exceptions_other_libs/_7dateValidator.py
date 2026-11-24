# 7. Write a program to validate dates in a file line by line using try-except-finally.
# Input: (dates.txt 4 10-05-2026 29-02-1909 32-07-2006 29-02-2024), (d.txt 1 15-08-2023)
# Output:
#   Run 1:
#   Valid date: 10-05-2026
#   Invalid date: 29-02-1909
#   Invalid date: 32-07-2006
#   Valid date: 29-02-2024
#   File closed successfully in finally block
#   Run 2:
#   Valid date: 15-08-2023
#   File closed successfully in finally block

from datetime import datetime

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
