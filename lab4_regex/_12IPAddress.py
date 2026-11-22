# 12. Write a program to validate and extract octets of an IPv4 address using regular expressions.
# Input: (192.168.1.1), (999.999.999.999)
# Output: 192 168 1 1, Invalid

import re

ip = input("Enter IPV4 address: ")
octet = r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
match = re.search(rf"\b({octet})\.({octet})\.({octet})\.({octet})\b", ip)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")