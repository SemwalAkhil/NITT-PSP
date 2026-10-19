#Vehicle number TN45AB1234
import re

text = input("Text: ")
match = re.search(r"\b([A-Z]{2})(\d{2})([A-Z]{2})(\d{4})\b", text)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Not found")