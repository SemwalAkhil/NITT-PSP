# 6. Write a program to record expenses by date and calculate monthly and date-wise totals using dictionaries.
# Input: (6 17-01-2026 "500 1000 2000" 29-01-2026 "100 200" 22-02-2026 "50 50" 04-03-2026 "100 100" 05-04-2026 "50 2000" 06-04-2026 "400 1600"), (2 01-01-2026 "100 200" 02-02-2026 "300")
# Output:
#   Run 1:
#   17-01-2026: 3500
#   29-01-2026: 300
#   {'01': 3800, '02': 100, '03': 200, '04': 4050}
#   Run 2:
#   01-01-2026: 300
#   02-02-2026: 300
#   {'01': 300, '02': 300}

n = int(input("Enter number of dates: "))
expenses = {}
for i in range(n):
    d = input("Enter date (DD-MM-YYYY): ")
    amts = [int(x) for x in input("Enter expense amounts: ").split()]
    expenses[d] = amts

total_per_date = {
    date:0 for date in expenses.keys()
}
for date,amounts in expenses.items():
    for amount in amounts:
        total_per_date[date] += amount 

for date,amount in total_per_date.items():
    print(f"{date}: {amount}")

total_per_month = {i.split("-")[1]:0 for i in expenses.keys()}

for date,amount in total_per_date.items():
    total_per_month[date.split("-")[1]] += amount

print(total_per_month)
