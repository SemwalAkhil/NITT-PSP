import re
url = input("Enter URL: ")
match = re.match(r"([A-Za-z][A-Za-z0-9\+\.\-])+://([A-Za-z0-9-\.]{,255})",url)

if match:
    print("Valid URL")
    print("Protocol: ",match.group(1))
    print("Domain: ",match.group(2))
    print("Path: ",match.group(3))
else:
    print("Invalid URL")