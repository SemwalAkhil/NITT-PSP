def findY(x:int,n:int)->float:
    if n == 0:
        return x
    elif n == 1:
        return x + 1
    elif n == 2:
        return x**2 + n
    return x**n

if __name__ == "__main__":
    x:int = int(input("Enter X: "))
    n:int = int(input("Enter N: "))
    print("Y : ",findY(x,n))