# Regular expression for phone number 91-044-1234-5678
import re
phoneNumber = input("Enter landline number (xx-xxx-xxxx-xxxx): ")
match = re.search(r"(\d{2})-(\d{3})-(\d{4}-\d{4})", phoneNumber)
if match:
    print(f"Country Code: {match.group(1)}")
    print(f"Area Code: {match.group(2)}")
    print(f"Number: {match.group(3)}")
else:
    print("Invalid")
