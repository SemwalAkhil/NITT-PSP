P = float(input("Enter principal amount: "))
R = float(input("Enter annual rate of interest (%): "))
t = float(input("Enter time in years: "))

r = R / (12 * 100)
n = t * 12

emi = (P * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
print("Monthly EMI: ", emi)
