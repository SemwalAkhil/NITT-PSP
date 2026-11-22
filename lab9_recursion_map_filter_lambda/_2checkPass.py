# 2. Write a program to evaluate password strengths into a dictionary using map and lambda.
# Input: None (data defined in the script)
# Output: {'c112tl109nt115y': False, 'T98eF99nM114rC111d': True, 'P97eE116sL109nU100rM111n': True, 'G101nT103rS110sA116tM105t': True, 'b117ec102er110sb111es114e': False, 'o115dr114ds116em97a': False}

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
