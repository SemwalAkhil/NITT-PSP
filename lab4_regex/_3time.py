# 10:23:45 A.M or 10:23:45 P.M
import re

match = re.fullmatch(r"(0[1-9]|1[0-2]):([0-5]\d):([0-5]\d) ([AP]\.M)", input("Time: ").strip())
print(*match.groups() if match else ["Invalid"])
