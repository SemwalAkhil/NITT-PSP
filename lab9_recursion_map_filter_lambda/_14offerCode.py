# 14. Write a program to compute prices after applying a 10% discount using map and lambda.
# Input: None (data defined in the script)
# Output: 1350.0 1980.0 900.0 1800.0 2970.0

prices = [1500,2200,1000,2000,3300]
print(" ".join(map(lambda x: str(x*0.9),prices)))