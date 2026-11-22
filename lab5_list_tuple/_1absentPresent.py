# 1. Write a program to count the number of present and absent records from a status list.
# Input: None (data defined in the script)
# Output: 6 12

status = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
print(status.count(1), status.count(0))