# 9. Write a program to compute datewise and overall expenses from a flattened expense list.
# Input: None (data defined in the script)
# Output:
#   01-10-2026 : 800
#   02-10-2026 : 900
#   03-10-2026 : 1000
#   Overall expense: 2700

expenses = [
    '01-10-2026', 500,
    '01-10-2026', 300,
    '02-10-2026', 700,
    '02-10-2026', 200,
    '03-10-2026', 1000
]

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