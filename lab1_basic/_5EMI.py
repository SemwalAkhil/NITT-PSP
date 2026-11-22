# 5. Write a program to calculate monthly EMI given principal, annual interest rate, and time in years.
# Input: (100000 10 1), (50000 12 2)
# Output: Monthly EMI:  8791.58872300099, Monthly EMI:  2353.6736111632335

P = float(input("Enter principal amount: "))
R = float(input("Enter annual rate of interest (%): "))
t = float(input("Enter time in years: "))

r = R / (12 * 100)
n = t * 12

emi = (P * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
print("Monthly EMI: ", emi)
