import csv

filename = "expenses.csv"
sample_data = [
    ["17-01-2026", "500"],
    ["17-01-2026", "1000"],
    ["29-01-2026", "200"],
    ["22-02-2026", "bad_amount"],
    ["22-02-2026", "150"]
]

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
