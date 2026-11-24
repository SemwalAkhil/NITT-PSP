def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input("Enter number of terms: "))
g = fib()
print([next(g) for _ in range(n)])
