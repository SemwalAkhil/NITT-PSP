# anusenthil@gmail.com
import re

email = input("Email id: ")
match = re.search(r"([\w.-]+)@([\w.-]+\.\w+)", email)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Not found")