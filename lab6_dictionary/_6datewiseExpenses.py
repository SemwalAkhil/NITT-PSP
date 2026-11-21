expenses = {
    "17-01-2026":[500,1000,2000],
    "29-01-2026":[100,200],
    "22-02-2026":[50,50],
    "04-03-2026":[100,100],
    "05-04-2026":[50,2000],
    "06-04-2026":[400,1600],
}
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