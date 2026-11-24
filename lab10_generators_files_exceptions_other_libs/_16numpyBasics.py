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
