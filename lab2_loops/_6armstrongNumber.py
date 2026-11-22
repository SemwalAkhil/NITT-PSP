# 6. Write a program to check whether a given number is an Armstrong number.
# Input: (153), (123)
# Output: Armstrong, Not Armstrong

temp = num = int(input("Enter number : "))
digits = []
sum = 0
while (num != 0):
    digits.append(num % 10)
    num //= 10
for i in digits:
    sum += i ** len(digits)
if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")