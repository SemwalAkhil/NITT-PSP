from _1passphraseToPassword import passwordToPassphrase
import re
def checkPass(password:str):    
    return {password:False} if (re.search(r"[a-z]",password) == None) else {password:False} if re.search(r"[A-Z]",password) == {password:False} else {password:False} if (len(password) < 8) else {password:True}
    

if __name__ == "__main__":
    print("{}".format(checkPass(passwordToPassphrase()).items()))
