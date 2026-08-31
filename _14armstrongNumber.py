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