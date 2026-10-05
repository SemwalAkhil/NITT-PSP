a = float(input("enter coefficient of x^2 : "))
b = float(input("enter coefficient of x : "))
c = float(input("enter constant : "))

print("Roots are: ",(-b + (b**2 - 4 * a *c)**(1/2))/2 * a," ",(-b - (b**2 - 4 * a *c)**(1/2))/2 * a)