# 5. Write a program to find the area of a triangle given its three sides.
# Input: (3 4 5), (5 12 13)
# Output: Area:  6.0, Area:  30.0

a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))
s = (a+b+c)/2
print("Area: ",(s*(s-a)*(s-b)*(s-c))**(1/2))