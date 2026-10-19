import re

currency = input("Enter string with currency: ")
matches = re.findall(r"(?:₹|Rs\.?|\$|€|£)\s*\d+(?:,\d{3})*(?:\.\d{1,2})?", currency)

if matches:
    for match in matches:
        print(match, end=" ")
else:
    print("Not found")