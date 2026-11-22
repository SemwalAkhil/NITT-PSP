# 4. Write a function to check password strength based on length, cases, digits, and special characters.
# Input: p="Pass@1234", p="weak"
# Output: Pass@1234 : True, weak : False

import re

def checkPass(password: str):
    if (len(password) >= 8 and re.search(r"\d", password)
        and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)
        and re.search(r"[^A-Za-z0-9\s]", password)):
        return True
    return False

if __name__ == "__main__":
    p = "Pass@1234"
    print(p, ":", checkPass(p))
    print("weak", ":", checkPass("weak"))
