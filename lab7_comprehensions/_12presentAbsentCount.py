# 12. Write a program to read attendance status values and count absent and present counts using list comprehension.
# Input: ("0 1 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0"), ("1 1 0")
# Output:
#   Present: 6
#   Absent: 12

abs_list = [int(x) for x in input("Enter status values (0 for absent, 1 for present): ").split()]
absent = len([i for i in abs_list if i == 0])
present = len([i for i in abs_list if i == 1])
print(f"Present: {present}")
print(f"Absent: {absent}")
