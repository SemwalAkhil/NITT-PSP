# 12. Write a generator function to yield terms of the Fibonacci sequence.
# Input: (7), (5)
# Output: [0, 1, 1, 2, 3, 5, 8], [0, 1, 1, 2, 3]

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

n = int(input("Enter number of terms: "))
g = fib()
print([next(g) for _ in range(n)])
