# 5. Write a program to validate and extract username and domain from an email ID using regex.
# Input: (anusenthil@gmail.com), (invalid_email)
# Output: anusenthil gmail.com, Not found

import re

email = input("Email id: ")
match = re.search(r"([\w.-]+)@([\w.-]+\.\w+)", email)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Not found")