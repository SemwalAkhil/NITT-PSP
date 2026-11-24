# 13. Write a generator function to yield squares of natural numbers.
# Input: (7), (4)
# Output: [1, 4, 9, 16, 25, 36, 49], [1, 4, 9, 16]

def squares():
    n = 1
    while True:
        yield n * n
        n += 1

n = int(input("Enter number of terms: "))
g = squares()
print([next(g) for _ in range(n)])
