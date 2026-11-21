armstrongs = list(filter(lambda n: sum(int(d)**3 for d in str(n)) == n, range(100, 1000)))
print(armstrongs)
