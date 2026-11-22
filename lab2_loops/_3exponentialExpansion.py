# 3. Write a program to calculate the Taylor series expansion of e^x using loops.
# Input: (1), (2)
# Output: MY = 2.718282, MY = 7.389056

from math import factorial, exp, fabs
# sum (x^n/n!) = e^x

x: float = float(input("Enter value of x in e^x: "))
sum: float = 0
i: int = 0
term: float = (x ** i)/factorial(i)
accuracy: int = 6

print("\n============ CALCULATIONS ===============\n")
while fabs(term) > 10**(-accuracy):
    term = (x ** i)/factorial(i)
    print("{:.6f} = <{}> {}^{}/{}!".format(term, i+1, x, i, i))
    sum = sum + term
    i += 1
print("\n=========================================\n")
print("\nMY = {:.6f}\nActual = {:.6f}".format(sum, exp(x)))
