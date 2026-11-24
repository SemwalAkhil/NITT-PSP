def squares():
    n = 1
    while True:
        yield n * n
        n += 1


g = squares()
print([next(g) for _ in range(7)])  
