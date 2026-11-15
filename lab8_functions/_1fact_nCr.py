# write a function to calculate the factorial and ncr
def factorial(num:int):
    if num > 0:
        return num * factorial(num-1)
    else :
        return 1

def ncr(n,r):
    if (0 <= r <= n):
        return factorial(n)/(factorial(r)*factorial(n-r))
    else:
        return 1

if __name__ == "__main__":
    n = 5
    r = 2
    print(f"Factorial {n}: {factorial(n)}")
    print(f"nCr {n}C{r}: {ncr(n,r)}")