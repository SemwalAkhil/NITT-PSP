# 2. Write a program to generate a list of cubes of even natural numbers up to N using list comprehension.
# Input: (6), (4)
# Output: [8, 64, 216], [8, 64]

print([natural ** 3 for natural in range(1,int(input("Enter number of natural numbers: "))+1) if natural % 2 == 0])
