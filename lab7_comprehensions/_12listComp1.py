# 12. Write a program to count absent and present counts from a status list using list comprehension.
# Input: None (data defined in the script)
# Output:
#   Present: 6
#   Absent: 12

abs_list = [0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,1,0,0]
absent = len([i for i in abs_list if i == 0])
present = len([i for i in abs_list if i == 1])
print(f"Present: {present}")
print(f"Absent: {absent}")