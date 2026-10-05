import re
ip = input("Enter IPV4 address: ")
match = re.match(r"\d+\.\d+\.\d+\.\d",ip)
if match:
    print("Valid IP")
else:
    print("Invalid IP")