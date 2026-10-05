a = int(input("Side 1: "))
b = int(input("Side 2: "))
c = int(input("Side 3: "))
s = (a+b+c)/2
print("Area: ",(s*(s-a)*(s-b)*(s-c))**(1/2))