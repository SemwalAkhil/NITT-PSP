# 10:23:45 A.M or 10:23:45 P.M
import re
time = input("Enter time (hh:mm:ss A.M): ")
match = re.search(
    r"(0[1-9]|1[0-2]):([0-5][0-9]|60):([0-5][0-9]|60) (A\.M|P\.M)", time)
print("Hours  : ", match.group(1))
print("Minutes: ", match.group(2))
print("Seconds: ", match.group(3))
print("A.M/P.M: ", match.group(4))
