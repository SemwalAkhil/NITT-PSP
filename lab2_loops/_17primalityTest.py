# 17. Write a program to check if a number is prime using a for-else loop.
# Input: (11), (12)
# Output: Prime, Not prime

'''
check if a number is prime
'''
num: int = int(input("Enter a number: "))
for i in range(2, int(num**(1/2)) + 1):
    if (num % i == 0):
        print("Not prime")
        break
else:
    print("Prime")
