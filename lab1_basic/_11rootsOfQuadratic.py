a = float(input("enter coefficient of x^2 : "))
b = float(input("enter coefficient of x : "))
c = float(input("enter constant : "))

d = b**2 - 4 * a * c
if d < 0:
    print("No real roots")
else:
    print("Roots are: ",(-b + (d)**(1/2))/(2*a)," ",(-b - (d)**(1/2))/(2*a))