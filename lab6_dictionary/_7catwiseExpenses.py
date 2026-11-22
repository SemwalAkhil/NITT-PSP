# 7. Write a program to read category-tagged expenses from the user and compute total expenses grouped by category code.
# Input: (6 17-01-2026 3 1 500 1 1000 2 2000 29-01-2026 2 3 100 2 200 22-02-2026 2 3 50 1 50 04-03-2026 2 3 100 1 100 05-04-2026 2 3 50 2 2000 06-04-2026 2 1 400 3 1600), (1 01-01-2026 2 1 100 2 200)
# Output:
#   Category 1 : 2050
#   Category 2 : 4200
#   Category 3 : 1900

n = int(input("Enter number of dates: "))
expenses:dict[str,list[tuple[int,...]]] = {}
for i in range(n):
    d = input("Enter date (DD-MM-YYYY): ")
    k = int(input("Enter number of expenses for this date: "))
    day_list = []
    for j in range(k):
        cat = int(input("Enter category code: "))
        amt = int(input("Enter amount: "))
        day_list.append((cat, amt))
    expenses[d] = day_list

cat_expenses:dict[int,int] = {}
for date,expense in expenses.items():
    for exp in expense:
        if cat_expenses.get(exp[0],False):
            cat_expenses[exp[0]] += exp[1]
        else:
            cat_expenses[exp[0]] = exp[1]

for cat,expense in cat_expenses.items():
    print(f"Category {cat} : {expense}")
