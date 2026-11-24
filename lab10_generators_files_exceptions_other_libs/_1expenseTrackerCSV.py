# 1. Write a program to record expenses in a CSV file, calculate totals, and handle file and value errors.
# Input: (expenses.csv 3 17-01-2026 500 17-01-2026 1000 22-02-2026 bad_amount), (exp.csv 1 01-01-2026 200)
# Output:
#   Skipping invalid amount 'bad_amount' on date 22-02-2026
#   Datewise expenses:
#   17-01-2026: 1500.0
#   Overall expense: 1500.0

import csv

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
