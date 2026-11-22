# 2. Write a program to extract date, month, and year from a date string using regular expressions.
# Input: (23/04/1999), (invalid)
# Output:
#   Date: 23
#   Month: 04
#   Year: 1999

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
