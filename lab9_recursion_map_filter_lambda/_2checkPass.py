# 2. Write a program to evaluate password strengths into a dictionary using map and lambda.
# Input: (2 "carpet lemon thursday" "Table Falcon Mirror Cloud"), (1 "weakpass")
# Output: {'c112tl109nt115y': False, 'T98eF99nM114rC111d': True}, {'weakpass': False}

from _1passphraseToPassword import passphraseToPassword
import re

def checkPass(password:str):
    if (len(password) >= 8 and re.search(r"\d", password)
        and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        return True
    return False

if __name__ == "__main__":
    n = int(input("Enter number of passphrases: "))
    p_list = [input(f"Enter passphrase {i+1}: ") for i in range(n)]
    passwords = passphraseToPassword(p_list)
    pass_strength = dict(map(lambda p: (p, checkPass(p)), passwords))
    print(pass_strength)
