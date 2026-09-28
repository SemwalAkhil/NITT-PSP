# TN45AB1234
import re
vehicleNumber = input("Enter vehicle number (AB12CD3456): ")
match = re.search(r"([A-Z]{2})([0-9]{2})([A-Z]{2})([0-9]{4})", vehicleNumber)
print("State Code   : ", match.group(1))
print("District Code: ", match.group(2))
print("Series Code  : ", match.group(3))
print("Unique Number: ", match.group(4))
