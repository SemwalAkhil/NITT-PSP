import re

pid = input("Enter product ID: ")
match = re.search(r"\bPROD(\d{4})\b", pid)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")
