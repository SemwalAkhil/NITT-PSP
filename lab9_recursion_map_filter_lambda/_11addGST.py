# 11. Write a program to read prices and compute values including 18% GST using map and lambda.
# Input: ("1500 2200 1000 2000 3300"), ("100 200")
# Output: 1770.0 2596.0 1180.0 2360.0 3894.0, 118.0 236.0

prices = [float(x) for x in input("Enter prices: ").split()]
print(" ".join(map(lambda x: str(x*1.18),prices)))
