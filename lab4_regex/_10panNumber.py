import re

pan_num = input("Enter pan number: ")
match = re.search(r"\b([A-Z]{3})([PCHFATBGJL])([A-Z])(\d{4})([A-Z])\b", pan_num)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")