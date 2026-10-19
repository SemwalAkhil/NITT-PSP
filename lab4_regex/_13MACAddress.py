'''
INPUT:  mac(M)                                           00:1A:2B:3C:4D:5E
OUTPUT: result(R)                                        00:1A:2B 3C:4D:5E

INPUT:  mac(M)                                           00:1A:2B:3C:4D:5G
OUTPUT: result(R)                                        Invalid
'''
import re

mac = input("Enter MAC address: ").upper()
match = re.search(r"\b([0-9A-F]{2}(?:[:-][0-9A-F]{2}){2})[:-]([0-9A-F]{2}(?:[:-][0-9A-F]{2}){2})\b", mac)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")