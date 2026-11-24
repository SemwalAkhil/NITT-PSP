# 1. Write a program to calculate the factorial of a number and nCr using functions.
# Input: (5 2), (6 3)
# Output:
#   Run 1:
#   Factorial 5: 120
#   nCr 5C2: 10
#   Run 2:
#   Factorial 6: 720
#   nCr 6C3: 20

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
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))
    print(f"Factorial {n}: {factorial(n)}")
    print(f"nCr {n}C{r}: {ncr(n,r)}")
