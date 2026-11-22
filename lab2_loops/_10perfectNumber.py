# 10. Write a program to check whether a given number is a perfect number using loops.
# Input: (6), (10)
# Output: Perfect Number, Not Perfect Number

n:int = int(input("Enter a number: "))
s = 0
for i in range(1,n//2+1):
    s += i if n % i == 0 else 0
print("Perfect Number" if s == n else "Not Perfect Number")