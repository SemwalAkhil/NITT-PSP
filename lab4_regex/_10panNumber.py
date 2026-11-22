# 10. Write a program to validate and extract components of a PAN card number using regular expressions.
# Input: (ABCPA1234F), (INVALID123)
# Output: ABC P A 1234 F, Invalid

import re

pan_num = input("Enter pan number: ")
match = re.search(r"\b([A-Z]{3})([PCHFATBGJL])([A-Z])(\d{4})([A-Z])\b", pan_num)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")