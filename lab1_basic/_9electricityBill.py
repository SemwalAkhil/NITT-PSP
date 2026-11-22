# 9. Write a program to calculate the electricity bill for a given usage in units and cost per unit.
# Input: (150 6.5), (200 5.0)
# Output: Electricity bill:  975.0, Electricity bill:  1000.0

units = float(input("Enter units used: "))
cost = float(input("Enter cost per unit: "))
bill = units * cost
print("Electricity bill: ", bill)
