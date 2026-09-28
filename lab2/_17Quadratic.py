a = int(input("enter coefficient of x^2 : "))
b = int(input("enter coefficient of x : "))
c = int(input("enter constant : "))

print("Roots are: ",(-b + (b**2 - 4 * a *c))/2 * a," ",(-b - (b**2 - 4 * a *c))/2 * a)