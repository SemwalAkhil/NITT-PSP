# 12. Write a program to find the remaining water in a leaking tank after a given number of days.
# Input: (1000 0.01 1), (500 0.05 2)
# Output: Remaining water in tank:  136.0000000000001, Remaining water in tank:  0

capacity = float(input("Enter tank capacity (litres): "))
leak = float(input("Enter leak per second (litres): "))
days = float(input("Enter number of days: "))

remaining = capacity - (leak * days * 24 * 60 * 60)
if remaining < 0:
    remaining = 0
print("Remaining water in tank: ", remaining)
