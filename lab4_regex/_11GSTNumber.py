# 11. Write a program to validate and extract components of a GSTIN using regular expressions.
# Input: (22AAAAA0000A1Z5), (INVALIDGST)
# Output: 22 AAAAA0000A 1 5, Invalid

import re

gst_num = input("Enter GST number: ")
match = re.search(r"\b(\d{2})([A-Z]{5}\d{4}[A-Z])([1-9A-Z])Z([A-Z0-9])\b", gst_num)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")