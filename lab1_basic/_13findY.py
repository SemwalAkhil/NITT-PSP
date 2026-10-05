x:int = int(input("Enter X: "))
n:int = int(input("Enter N: "))

if n == 0:
    print("Y : ",x)
elif n == 1:
    print("Y : ",x+1)
elif n == 2:
    print("Y : ",x**2 + n)
else:
    print("Y : ",x**n)


