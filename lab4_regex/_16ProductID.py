# 16. Write a program to validate a product ID of the form PRODXXXX using regular expressions.
# Input: (PROD1234), (PROD12)
# Output: 1234, Invalid

import re

pid = input("Enter product ID: ")
match = re.search(r"\bPROD(\d{4})\b", pid)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")
