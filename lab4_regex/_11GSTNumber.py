import re

gst_num = input("Enter GST number: ")
match = re.search(r"\b(\d{2})([A-Z]{5}\d{4}[A-Z])([1-9A-Z])Z([A-Z0-9])\b", gst_num)

if match:
    for item in match.groups():
        print(item, end=" ")
else:
    print("Invalid")