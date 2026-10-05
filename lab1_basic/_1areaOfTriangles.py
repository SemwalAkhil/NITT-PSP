a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))
s = (a+b+c)/2
A = (s*(s-a)*(s-b)*(s-c)) ** (1/2)
print("Area of triangle: ",A)