# find nth armstrong number

num: int = int(input("Enter N: "))
counter: int = 0
check: int = 1
while counter != num:
    digits = []
    while check != 0:
        digits.append(check % 10)
        check //= 10
