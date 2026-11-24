# 2. Write a program using regular expressions to validate and parse a date in DD/MM/YYYY format.
# Input: (23/04/1999), (invalid)
# Output:
#   Run 1:
#   Date: 23
#   Month: 04
#   Year: 1999
#   Run 2:
#   Invalid

import re
date = input("Enter date: ")
match = re.search(
    r"(\d{2})(/|-|\.)(\d{2}|[A-Za-z]{3})\2(\d{4})", date)
if match:
    print(f"Date: {match.group(1)}")
    print(f"Month: {match.group(3)}")
    print(f"Year: {match.group(4)}")
else:
    print("Invalid")
