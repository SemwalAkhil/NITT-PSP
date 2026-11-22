# 11. Write a program to find the roots of a quadratic equation.
# Input: (1 -3 2), (1 2 5)
# Output: Roots are:  2.0   1.0, No real roots

a = float(input("enter coefficient of x^2 : "))
b = float(input("enter coefficient of x : "))
c = float(input("enter constant : "))

d = b**2 - 4 * a * c
if d < 0:
    print("No real roots")
else:
    print("Roots are: ",(-b + (d)**(1/2))/(2*a)," ",(-b - (d)**(1/2))/(2*a))