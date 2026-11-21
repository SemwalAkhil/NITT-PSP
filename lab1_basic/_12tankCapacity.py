capacity = float(input("Enter tank capacity (litres): "))
leak = float(input("Enter leak per second (litres): "))
days = float(input("Enter number of days: "))

remaining = capacity - (leak * days * 24 * 60 * 60)
if remaining < 0:
    remaining = 0
print("Remaining water in tank: ", remaining)
