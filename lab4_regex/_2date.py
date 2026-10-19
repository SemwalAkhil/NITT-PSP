# 23/04/1999 or 23-Jan-2021
import re
date = input("Enter date: ")
match = re.search(
    r"(\d{2})(/|-|\.)(\d{2}|[A-Za-z]{3})\2(\d{4})", date)
print(f"Date: {match.group(1)}")
print(f"Month: {match.group(3)}")
print(f"Year: {match.group(4)}")
