expenses:dict[str:list[tuple[int]]] = {
    "17-01-2026":[(1,500),(1,1000),(2,2000)],
    "29-01-2026":[(3,100),(2,200)],
    "22-02-2026":[(3,50),(1,50)],
    "04-03-2026":[(3,100),(1,100)],
    "05-04-2026":[(3,50),(2,2000)],
    "06-04-2026":[(1,400),(3,1600)],
}
cat_expenses:dict[int:int] = {}
for date,expense in expenses.items():
    for exp in expense:
        if cat_expenses.get(exp[0],False):
            cat_expenses[exp[0]] += exp[1]
        else:
            cat_expenses[exp[0]] = exp[1]

for cat,expense in cat_expenses.items():
    print(f"Category {cat} : {expense}")
