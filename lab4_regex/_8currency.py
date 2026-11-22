# 8. Write a program to find all currency amounts in a text string using regular expressions.
# Input: ("Price is Rs. 500 and Rs. 1000"), ("No currency here")
# Output: Rs. 500 Rs. 1000, Not found

import re

currency = input("Enter string with currency: ")
matches = re.findall(r"(?:₹|Rs\.?|\$|€|£)\s*\d+(?:,\d{3})*(?:\.\d{1,2})?", currency)

if matches:
    for match in matches:
        print(match, end=" ")
else:
    print("Not found")