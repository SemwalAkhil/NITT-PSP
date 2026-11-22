# 9. Write a program to read expenses from the user and compute datewise and overall expenses.
# Input: (5 01-10-2026 500 01-10-2026 300 02-10-2026 700 02-10-2026 200 03-10-2026 1000), (2 01-10-2026 400 02-10-2026 600)
# Output:
#   01-10-2026 : 800
#   02-10-2026 : 900
#   03-10-2026 : 1000
#   Overall expense: 2700

n = int(input("Enter number of expenses: "))
expenses = []
for i in range(n):
    d = input("Enter date (DD-MM-YYYY): ")
    amt = int(input("Enter amount: "))
    expenses.append(d)
    expenses.append(amt)

dates = []
total = 0

for i in range(0, len(expenses), 2):
    date = expenses[i]
    amount = expenses[i + 1]
    total += amount

    if date not in dates:
        dates.append(date)
        day_total = 0

        for j in range(0, len(expenses), 2):
            if expenses[j] == date:
                day_total += expenses[j + 1]

        print(date, ":", day_total)

print("Overall expense:", total)
