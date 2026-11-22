# 4. Write a program to validate and extract vehicle registration components using regular expressions.
# Input: (TN45AB1234), (INVALID)
# Output: TN 45 AB 1234, Not found

import re

text = input("Text: ")
match = re.search(r"\b([A-Z]{2})(\d{2})([A-Z]{2})(\d{4})\b", text)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Not found")