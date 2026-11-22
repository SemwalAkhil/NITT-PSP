# 4. Write a program to calculate the total cost of fencing a rectangular field.
# Input: (10 20 5), (15 25 10)
# Output: Total fencing cost: 300.0, Total fencing cost: 800.0

L = float(input("Length of field: "))
B = float(input("Breadth of field: "))
C= float(input("Fencing cost per unit: "))
T = 2 * (L+B) * C
print(f"Total fencing cost: {T}")