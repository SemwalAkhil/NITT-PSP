def squares():
    n = 1
    while True:
        yield n * n
        n += 1

n = int(input("Enter number of terms: "))
g = squares()
print([next(g) for _ in range(n)])
