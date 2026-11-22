# 9. Write functions to add expenses, calculate total expense, and calculate datewise expense totals.
# Input: (3 01-10-2026 500 01-10-2026 300 02-10-2026 700), (1 01-01-2026 100)
# Output:
#   Datewise:  {'01-10-2026': 800, '02-10-2026': 700}
#   Total:  1500

def addExpense(expenses: dict, date: str, amount: int):
    if date in expenses:
        expenses[date].append(amount)
    else:
        expenses[date] = [amount]

def totalExpense(expenses: dict):
    total = 0
    for amounts in expenses.values():
        total += sum(amounts)
    return total

def datewiseTotal(expenses: dict):
    totals = {}
    for date, amounts in expenses.items():
        totals[date] = sum(amounts)
    return totals

if __name__ == "__main__":
    exp = {}
    n = int(input("Enter number of expenses: "))
    for i in range(n):
        d = input("Enter date (DD-MM-YYYY): ")
        amt = int(input("Enter amount: "))
        addExpense(exp, d, amt)
    print("Datewise: ", datewiseTotal(exp))
    print("Total: ", totalExpense(exp))
