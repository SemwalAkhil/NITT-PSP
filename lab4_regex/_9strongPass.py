import re

password = input("Enter a password: ")
if (len(password) >= 8 and re.search(r"\d", password)
    and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)
    and re.search(r"[^A-Za-z0-9\s]", password)):
    print("Strong")
else:
    print("Weak")