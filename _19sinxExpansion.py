from myMath import factorial
# sum (-1)^(n-1) * x ^ (2n-1) / (2n - 1)!

num: int = int(
    input("Enter number of terms to which expansion to be calculated: "))
x: float = float(input("Enter value of x in radians: "))
sum: float = 0
for i in range(1, num):
    sum = sum + (-1)**(i-1) * ((x ** (2*i-1))/factorial((2*i-1)))
    print("<{}> (-1)^{} * {} ^ {} / {}!".format(i,i-1, x, 2 * i - 1, 2 * i - 1))

print("\n{}".format(sum))
