# 3. Write a program to filter strong passwords from a dictionary using filter and lambda.
# Input: (2 "carpet lemon thursday" "Table Falcon Mirror Cloud"), (1 "weakpass")
# Output: Strong passwords:  ['T98eF99nM114rC111d'], Strong passwords:  []

from _1passphraseToPassword import passphraseToPassword
from _2checkPass import checkPass

if __name__ == "__main__":
    n = int(input("Enter number of passphrases: "))
    p_list = [input(f"Enter passphrase {i+1}: ") for i in range(n)]
    passwords = passphraseToPassword(p_list)
    pass_strength = dict(map(lambda p: (p, checkPass(p)), passwords))
    strong_passwords = list(filter(lambda p: pass_strength[p], pass_strength))
    print("Strong passwords: ", strong_passwords)
