# 12. Write a program to generate a password from a passphrase using character transformations.
# Input: ("hello world"), ("good morning")
# Output: Password is:  O104bD119h, Password is:  D103eG109d

inputStr = input("Enter pass phrase: ")
words = inputStr.split()
passw = ""
for word in words:
    passw += word[-1].upper() + str(ord(word[0])) + \
        chr(ord(word[len(word)//2]) - 10)
print("Password is: ", passw)
