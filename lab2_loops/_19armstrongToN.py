# 19. Write a program to find the Nth Armstrong number using loops.
# Input: (5), (10)
# Output: 5 armstrong number is : 5, 10 armstrong number is : 153

num: int = int(input("Enter N: "))
counter: int = 0
check: int = 1
while counter != num:
    temp = check
    digits = []
    while temp != 0:
        digits.append(temp % 10)
        temp //= 10
    sum_digits = 0
    for d in digits:
        sum_digits += d ** len(digits)
    if sum_digits == check:
        counter += 1
        if counter == num:
            print(f"{num} armstrong number is : {check}")
            break
    check += 1
