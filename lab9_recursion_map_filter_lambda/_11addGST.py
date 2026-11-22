# 11. Write a program to compute prices including 18% GST using map and lambda.
# Input: None (data defined in the script)
# Output: 1770.0 2596.0 1180.0 2360.0 3894.0

prices = [1500,2200,1000,2000,3300]
print(" ".join(map(lambda x: str(x*1.18),prices)))