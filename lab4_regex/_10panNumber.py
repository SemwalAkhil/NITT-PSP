import re
pan_num = input('Enter pan number: ')
match = re.match(r"([A-Z]{3})([PCHFATBGJL])([A-Z])([0-9]{4})([A-Z])",pan_num)
if match:
    print("Valid pan number")
    print(f"Series: {match.group(1)}")
    print(f"Type: {match.group(2)}")
    print(f"Surname First Letter: {match.group(3)}")
    print(f"Sequential Number: {match.group(4)}")
    print(f"Check Code: {match.group(5)}")
else:
    print("Invalid pan number")
