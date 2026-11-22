# 5. Write a program to reverse a given integer using a while loop.
# Input: (1234), (500)
# Output: Reverse is :  4321, Reverse is :  5

num = int(input("Enter number: "))
rev = 0
while (num != 0):
    rev = rev*10 + num % 10
    num //= 10
print("Reverse is : ",rev)