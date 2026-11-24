# 16. Write a program to demonstrate 2D NumPy array creation, shape, sum, mean, and transpose.
# Input: (2 3 "1 2 3 4 5 6"), (2 2 "1 0 0 1")
# Output:
#   Run 1:
#   Array:
#   [[1 2 3]
#    [4 5 6]]
#   Shape: (2, 3)
#   Sum: 21
#   Mean: 3.5
#   Row sums (axis=1): [ 6 15]
#   Column sums (axis=0): [5 7 9]
#   Transpose:
#   [[1 4]
#    [2 5]
#    [3 6]]
#   Run 2:
#   Array:
#   [[1 0]
#    [0 1]]
#   Shape: (2, 2)
#   Sum: 2
#   Mean: 0.5
#   Row sums (axis=1): [1 1]
#   Column sums (axis=0): [1 1]
#   Transpose:
#   [[1 0]
#    [0 1]]

import numpy as np

r = int(input("Enter rows: "))
c = int(input("Enter columns: "))
print(f"Enter {r * c} elements separated by space:")
vals = [int(x) for x in input().split()]
a = np.array(vals).reshape(r, c)

print("Array:")
print(a)
print("Shape:", a.shape)
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Row sums (axis=1):", np.sum(a, axis=1))
print("Column sums (axis=0):", np.sum(a, axis=0))
print("Transpose:")
print(a.T)
