from _1passphraseToPassword import passphraseToPassword
from _2checkPass import checkPass

if __name__ == "__main__":
    passwords = passphraseToPassword()
    pass_strength = dict(map(lambda p: (p, checkPass(p)), passwords))
    strong_passwords = list(filter(lambda p: pass_strength[p], pass_strength))
    print("Strong passwords: ", strong_passwords)
