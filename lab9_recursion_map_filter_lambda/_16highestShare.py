# 16. Write a program to find the highest share value from a list using functools.reduce and lambda.
# Input: None (data defined in the script)
# Output: Highest: 2000

import functools as f
shares = [1000,1100,1040,1913,2000,1445]
print(f"Highest: {f.reduce(lambda x,y: x if x > y else y,shares)}")