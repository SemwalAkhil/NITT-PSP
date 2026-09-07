'''
PROBLEM STATEMENT: Given a passphrase, create a password
INPUT: Passphrase (P)
OUTPUT: Password (O)
Read P
Words <- P.split()
O <- ""
For word in Words do
|   O += word.last_letter.upper + word.first_letter + (word.mid_letter.ascii - 10).character
Write O 
'''


def passToPassphrase(string: str) -> str:
    words = string.split()
    passw = ""
    for word in words:
        passw += word[-1].upper() + str(ord(word[0])) + \
            chr(ord(word[len(word)//2]) - 10)
    return passw


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


inputStr = input("Enter pass phrase: ")
password = passToPassphrase(inputStr)
print("Password is: ", password)
print("Password is: ", "Strong" if checkStrongPass(password) else "Weak")
print("Input String is: ", "Strong" if checkStrongPass(inputStr) else "Weak")
