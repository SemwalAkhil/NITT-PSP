# check password strength, make a password:strength dictionary, filter strong passwords and return a list of strong passwords
from _1passphraseToPassword import passphraseToPassword
import re

def checkPass(password:str):
    if (len(password) >= 8 and re.search(r"\d", password)
        and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        return True
    return False

if __name__ == "__main__":
    passwords = passphraseToPassword()
    pass_strength = dict(map(lambda p: (p, checkPass(p)), passwords))
    print(pass_strength)
