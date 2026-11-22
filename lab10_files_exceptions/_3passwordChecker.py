# 3. Write a program to read passwords from a text file, check strength, and write a report to another file.
# Input: (passwords.txt password_report.txt 3 Pass@1234 weakpass Secure#99), (pw.txt rep.txt 1 test)
# Output:
#   Report written to password_report.txt:
#   Pass@1234: Strong
#   weakpass: Weak
#   Secure#99: Strong

import re

def is_strong(password: str):
    return (len(password) >= 8 and re.search(r"\d", password)
            and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)
            and re.search(r"[^A-Za-z0-9\s]", password))

in_file = input("Enter input passwords filename: ")
out_file = input("Enter output report filename: ")
n = int(input("Enter number of passwords: "))
with open(in_file, "w") as f:
    for i in range(n):
        f.write(input("Enter password: ") + "\n")

try:
    with open(in_file, "r") as fin, open(out_file, "w") as fout:
        for line in fin:
            p = line.strip()
            if not p:
                continue
            status = "Strong" if is_strong(p) else "Weak"
            fout.write(f"{p}: {status}\n")
    print(f"Report written to {out_file}:")
    with open(out_file, "r") as f:
        print(f.read().strip())
except FileNotFoundError:
    print("Password file not found")
