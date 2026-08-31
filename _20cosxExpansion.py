from myMath import factorial
# sum (-1)^(n) * x ^ (2n) / (2n)!

num: int = int(
    input("Enter number of terms to which expansion to be calculated: "))
x: float = float(input("Enter value of x in radians: "))
sum: float = 0
for i in range(0, num):
    sum = sum + (-1)**(i) * ((x ** (2*i))/factorial((2*i)))
    print("<{}> (-1)^{} * {} ^ {} / {}!".format(i+1, i, x, 2 * i, 2 * i))

print("\n{}".format(sum))
