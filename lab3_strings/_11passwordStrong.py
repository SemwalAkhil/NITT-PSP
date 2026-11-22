# 11. Write a program to check if a password is strong (has length >= 8, uppercase, lowercase, digit).
# Input: (Abcdef1), (Abcdefg1)
# Output: Strong password:  False, Strong password:  True

strong = False
string = input("Enter password: ")
if len(string) >= 8:
    checkCaps = False
    checkLow = False
    checkNum = False
    strong = False
    counter = 0
    while (not strong and counter < len(string)):
        curr = string[counter]
        checkNum = checkNum or curr.isnumeric()
        checkCaps = checkCaps or curr.isupper()
        checkLow = checkLow or curr.islower()
        strong = checkCaps and checkLow and checkNum
        counter += 1

print("Strong password: ", strong)
