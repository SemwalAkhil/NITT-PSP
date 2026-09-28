from math import factorial, radians, fabs, cos
# sum (-1)^(n) * x ^ (2n) / (2n)!

x: float = radians(float(input("Enter value of x in degrees: ")))
sum: float = 0
i: int = 0
term: float = 1
accuracy: int = 6

print("\n============ CALCULATIONS ===============\n")
print("{:+.6f} = <{}> (-1)^{} * {} ^ {} / {}!".format(term,
                                                      i+1, i, x, 2 * i, 2 * i))
while fabs(term) > 10**(-accuracy):
    sum += term
    i += 1
    term = (-1)**(i) * ((x ** (2*i))/factorial((2*i)))
    print("{:+.6f} = <{}> (-1)^{} * {} ^ {} / {}!".format(term,
          i+1, i, x, 2 * i, 2 * i))
print("\n=========================================\n")
print("\nMY = {:.6f}\nActual = {:.6f}".format(sum, cos(x)))
