import re

ip = input("Enter IPV4 address: ")
octet = r"(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)"
match = re.search(rf"\b({octet})\.({octet})\.({octet})\.({octet})\b", ip)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")