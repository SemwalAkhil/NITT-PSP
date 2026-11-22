# 13. Write a program to calculate Y based on given values of X and N.
# Input: (3 2), (2 3)
# Output: Y :  11, Y :  8

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


