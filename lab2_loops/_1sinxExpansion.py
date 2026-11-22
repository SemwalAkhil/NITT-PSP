# 1. Write a program to calculate the Taylor series expansion of sin(x) using loops.
# Input: (30), (90)
# Output: MY = 0.500000, MY = 1.000000

from math import factorial, radians, fabs, sin

# sum (-1)^(n-1) * x ^ (2n-1) / (2n - 1)!

x: float = radians(float(input("Enter value of x in degrees: ")))
sum: float = 0
i: int = 1
term: float = (-1)**(i-1) * ((x ** (2*i-1))/factorial((2*i-1)))
accuracy: int = 6

print("\n============ CALCULATIONS ===============\n")
print("{:+.6f} = <{}> (-1)^{} * {} ^ {} / {}!".format(term, i,
                                                      i-1, x, 2 * i - 1, 2 * i - 1))
while fabs(term) > 10**(-accuracy):
    sum += term
    i += 1
    term = (-1)**(i-1) * ((x ** (2*i-1))/factorial((2*i-1)))
    print("{:+.6f} = <{}> (-1)^{} * {} ^ {} / {}!".format(term, i,
          i-1, x, 2 * i - 1, 2 * i - 1))
print("\n=========================================\n")
print("\nMY = {:.6f}\nActual = {:.6f}".format(sum, sin(x)))
