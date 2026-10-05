import re
currency = input("Enter string with currency: ")
matches = re.findall(r"\$\s*[0-9]+",currency)
for match in matches:
    print(match)
