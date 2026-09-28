'''
PROBLEM STATEMENT: Given a password check if it is strong or not
INPUT: Password (P)
OUTPUT: Strong (S)
Read P
If P.length < 8
|   S <- False
|   Write S
|   Exit
Check_Caps <- False
Check_Lower <- False
Check_Number <- False
S <- False
Counter <- 0
While S <- False and Counter < P.length do
|   S <- Check_Caps and Check_Lower and Check_Number
|   Current <- P[Counter]
|   Check_Number <- Check_Number or Current.is_number
|   Check_Caps <- Check_Caps or Current.is_upper
|   Check_Lower <- Check_Lower or Current.is_lower
|   Counter <- Counter + 1
Write S
'''


def checkStrongPass(string: str) -> bool:
    if len(string) < 8:
        return False
    checkCaps = False
    checkLow = False
    checkNum = False
    strong = False
    counter = 0

    while (not strong and counter < len(string)):
        # print(checkCaps, checkLow, checkNum)
        strong = checkCaps and checkLow and checkNum
        curr = string[counter]
        checkNum = checkNum or curr.isnumeric()
        checkCaps = checkCaps or curr.isupper()
        checkLow = checkLow or curr.islower()
        counter += 1

    return strong


password = input("Enter password: ")
print("Password is: ", "Strong" if checkStrongPass(password) else "Weak")
