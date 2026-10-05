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


inputStr = input("Enter pass phrase: ")
password = passToPassphrase(inputStr)
print("Password is: ", password)
