from myMath import factorial
# sum (x^n/n!) = e^x

num: int = int(
    input("Enter number of terms to which expansion to be calculated: "))
x: float = float(input("Enter value of x in e^x: "))
sum: float = 0
for i in range(0, num):
    sum = sum + (x ** i)/factorial(i)
    print("<{}> {}^{}/{}!".format(i+1, x, i, i))
print("\n{}".format(sum))
