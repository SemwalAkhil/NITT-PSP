# 3. Write a program to validate and extract components of a 12-hour time string using regex.
# Input: ("10:23:45 A.M"), ("25:00:00 P.M")
# Output: 10 23 45 A.M, Invalid

import re

match = re.fullmatch(r"(0[1-9]|1[0-2]):([0-5]\d):([0-5]\d) ([AP]\.M)", input("Time: ").strip())
print(*match.groups() if match else ["Invalid"])
