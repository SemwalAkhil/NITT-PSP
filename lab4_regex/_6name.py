# 6. Write a program to extract title and name components from a person's name using regular expressions.
# Input: ("Dr. (Mrs.) V. Priyadarshini"), ("Ram Kumar Verma")
# Output: Dr. Mrs. V. Priyadarshini, Ram Kumar Verma

import re

name = input("Enter name: ")
match = re.search(r"(Dr\.)?\s*\(?(Mr\.|Mrs\.|Ms\.)?\)?\s*([A-Za-z. ]+)", name)

if match:
    for item in match.groups():
        if item:
            print(item.strip(), end=" ")
else:
    print("Not found")