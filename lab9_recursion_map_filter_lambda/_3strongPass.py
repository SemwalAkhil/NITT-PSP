# 3. Write a program to filter strong passwords from a dictionary using filter and lambda.
# Input: None (data defined in the script)
# Output: Strong passwords:  ['T98eF99nM114rC111d', 'P97eE116sL109nU100rM111n', 'G101nT103rS110sA116tM105t']

from _1passphraseToPassword import passphraseToPassword
from _2checkPass import checkPass

if __name__ == "__main__":
    passwords = passphraseToPassword()
    pass_strength = dict(map(lambda p: (p, checkPass(p)), passwords))
    strong_passwords = list(filter(lambda p: pass_strength[p], pass_strength))
    print("Strong passwords: ", strong_passwords)
