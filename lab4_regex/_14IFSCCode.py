import re
ifsc = input("Enter IFSC code: ").upper()
match = re.match(r"([A-Z]{4})0([A-Z0-9]{6})",ifsc)
if match:
    print(f"Bank Name: {match.group(1)}")
    print(f"Branch Code: {match.group(2)}")