# 14. Write a program to read prices and compute values after applying a 10% discount using map and lambda.
# Input: ("1500 2200 1000 2000 3300"), ("100 200")
# Output: 1350.0 1980.0 900.0 1800.0 2970.0, 90.0 180.0

prices = [float(x) for x in input("Enter prices: ").split()]
print(" ".join(map(lambda x: str(x*0.9),prices)))
