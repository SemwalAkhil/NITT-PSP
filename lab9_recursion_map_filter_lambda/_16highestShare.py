# 16. Write a program to read share values and find the highest using functools.reduce and lambda.
# Input: ("1000 1100 1040 1913 2000 1445"), ("500 750 300")
# Output: Highest: 2000, Highest: 750

import functools as f
shares = [int(x) for x in input("Enter share values: ").split()]
print(f"Highest: {f.reduce(lambda x,y: x if x > y else y,shares)}")
