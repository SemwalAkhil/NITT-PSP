from math import log, fabs
# ln(1+x) = x - x^2/2 + x^3/3 - ...

x: float = float(input("Enter value of x (|x| < 1): "))
sum: float = 0
i: int = 1
term: float = x
accuracy: int = 6

print("\n============ CALCULATIONS ===============\n")
while fabs(term) > 10**(-accuracy):
    term = ((-1)**(i-1)) * (x**i) / i
    print("{:+.6f} = <{}> (-1)^{} * {}^{}/{}".format(term, i, i-1, x, i, i))
    sum += term
    i += 1
print("\n=========================================\n")
print("\nMY = {:.6f}\nActual = {:.6f}".format(sum, log(1 + x)))
