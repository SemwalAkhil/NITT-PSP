# 11. Write a decorator to measure and print the execution time of a function.
# Input: (10), (100)
# Output: Sum: 55, Sum: 5050

import time

def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        res = func(*args)
        print(f"Time: {time.perf_counter() - start:.6f}s")
        return res
    return wrapper

@timer
def total(n):
    return sum(range(n + 1))

n = int(input("Enter N: "))
print("Sum:", total(n))
