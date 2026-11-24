# 1. Write a program to record expenses in a CSV file, calculate totals, and handle file and value errors.
# Input: (1), (2)
# Output:
#   Run 1:
#   Datewise expenses:
#   17-01-2026: 1500.0
#   18-01-2026: 1000.0
#   19-01-2026: 300.0
#   20-01-2026: 600.0
#   21-01-2026: 1200.0
#   Overall expense: 4600.0
#   Run 2:
#   Skipping invalid amount 'abc' on date 17-01-2026
#   Skipping invalid amount 'bad_amount' on date 19-01-2026
#   Datewise expenses:
#   17-01-2026: 500.0
#   18-01-2026: 250.0
#   20-01-2026: 450.0
#   Overall expense: 1200.0

import csv
import os

sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data")
choice = input("Use sample data? (1 = clean, 2 = with errors, 0 = type my own): ").strip()

if choice == "1":
    filename = os.path.join(sample_dir, "expenses_clean.csv")
elif choice == "2":
    filename = os.path.join(sample_dir, "expenses_errors.csv")
else:
    filename = input("Enter CSV filename: ")
    n = int(input("Enter number of records: "))
    sample_data = []
    for i in range(n):
        d = input("Enter date (DD-MM-YYYY): ")
        amt = input("Enter amount: ")
        sample_data.append([d, amt])

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)

datewise = {}
overall = 0

try:
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            date, amt_str = row[0], row[1]
            try:
                amt = float(amt_str)
                overall += amt
                datewise[date] = datewise.get(date, 0) + amt
            except ValueError:
                print(f"Skipping invalid amount '{amt_str}' on date {date}")
except FileNotFoundError:
    print(f"File {filename} not found")

print("Datewise expenses:")
for date, total in datewise.items():
    print(f"{date}: {total}")
print(f"Overall expense: {overall}")
