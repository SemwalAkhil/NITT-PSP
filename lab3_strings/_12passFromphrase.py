inputStr = input("Enter pass phrase: ")
words = inputStr.split()
passw = ""
for word in words:
    passw += word[-1].upper() + str(ord(word[0])) + \
        chr(ord(word[len(word)//2]) - 10)
print("Password is: ", passw)
