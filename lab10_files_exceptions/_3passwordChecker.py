import re

def is_strong(password: str):
    return (len(password) >= 8 and re.search(r"\d", password)
            and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)
            and re.search(r"[^A-Za-z0-9\s]", password))

in_file = "passwords.txt"
out_file = "password_report.txt"

with open(in_file, "w") as f:
    f.write("Pass@1234\nweakpass\nSecure#99\n12345\n")

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
