# 1. Write a program to find the area of a triangle given its three sides.
# Input: (3 4 5), (6 8 10)
# Output: Area of triangle:  6.0, Area of triangle:  24.0

a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
s = (a+b+c)/2
A = (s*(s-a)*(s-b)*(s-c)) ** (1/2)
print("Area of triangle: ",A)