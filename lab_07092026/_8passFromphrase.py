def passToPassphrase(string:str)->str:
    words = string.split()
    passPhrase = ""
    for word in words:
        passPhrase += word[-1].upper() + str(ord(word[0])) + chr(ord(word[len(word)//2]) - 10)
    return passPhrase

def checkStrongPass(string:str)->bool:
    if len(string) < 8:
        return False
    checkCaps = False
    checkLow = False
    checkNum = False
    strong = False
    counter = 0

    while (not strong and counter < len(string)):
        print(checkCaps, checkLow, checkNum)
        strong = checkCaps and checkLow and checkNum
        curr = string[counter]
        checkNum = True if (checkNum or curr.isnumeric()) else False
        checkCaps = True if (checkCaps or curr.isupper()) else False
        checkLow = True if (checkLow or curr.islower()) else False
        counter += 1
    

    return strong

password = passToPassphrase(input("Enter pass phrase: "))
print("Password is: ",password)
print("Password is: ","Strong" if checkStrongPass(password) else "Weak")