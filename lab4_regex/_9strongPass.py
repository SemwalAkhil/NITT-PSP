import re
password = input("Enter a password: ")
if len(password) > 8:
    if re.findall(r"\d",password) and re.findall(r"[A-Z]",password) and re.findall(r"[a-z]",password) and re.findall(r"[^A-Za-z0-9\s]",password):
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak password")