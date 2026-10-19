'''
INPUT:  ifsc(I)                                          SBIN0001234
OUTPUT: result(R)                                        SBIN 0001234
INPUT:  ifsc(I)                                          SBIN1001234
OUTPUT: result(R)                                        Invalid
'''
import re

ifsc = input("Enter IFSC code: ").upper()
match = re.search(r"\b([A-Z]{4})0([A-Z0-9]{6})\b", ifsc)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")