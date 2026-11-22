# 1. Write functions to calculate the factorial of a number and nCr (combinations).
# Input: n=5, r=2
# Output:
#   Factorial 5: 120
#   nCr 5C2: 10

def factorial(num:int):
    if num > 0:
        return num * factorial(num-1)
    else :
        return 1

def ncr(n,r):
    if (0 <= r <= n):
        return factorial(n) // (factorial(r) * factorial(n-r))
    else:
        return 0

if __name__ == "__main__":
    n = 5
    r = 2
    print(f"Factorial {n}: {factorial(n)}")
    print(f"nCr {n}C{r}: {ncr(n,r)}")
