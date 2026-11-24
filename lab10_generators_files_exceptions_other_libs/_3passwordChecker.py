# 3. Write a program to validate passwords from a file and write a report of strong and weak passwords.
# Input: (1 report_clean.txt), (2 report_errors.txt)
# Output:
#   Pass@1234: Strong
#   weakpass: Weak
#   Secure#2026: Strong
#   admin: Weak
#   Python@Lab1: Strong
#   hello123: Weak
#   NITT#MCA26: Weak
#   qwerty: Weak
#   Super!Secret9: Strong

import re
import os

def is_strong(password: str):
    return (len(password) >= 8 and re.search(r"\d", password)
            and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)
            and re.search(r"[^A-Za-z0-9\s]", password))

sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data")
choice = input("Use sample data? (1 = clean, 2 = with errors, 0 = type my own): ").strip()

if choice == "1":
    in_file = os.path.join(sample_dir, "passwords_clean.txt")
elif choice == "2":
    in_file = os.path.join(sample_dir, "passwords_errors.txt")
else:
    in_file = input("Enter input passwords filename: ")
    out_file = input("Enter output report filename: ")
    n = int(input("Enter number of passwords: "))
    with open(in_file, "w") as f:
        for i in range(n):
            f.write(input("Enter password: ") + "\n")

if choice in ("1", "2"):
    out_file = input("Enter output report filename: ")

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
