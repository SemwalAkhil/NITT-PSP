# 12. Write a program to count present and absent values in a binary status list using comprehension.
# Input: ("0 1 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0"), ("1 1 0")
# Output:
#   Run 1:
#   Present: 6
#   Absent: 12
#   Run 2:
#   Present: 2
#   Absent: 1

abs_list = [int(x) for x in input("Enter status values (0 for absent, 1 for present): ").split()]
absent = len([i for i in abs_list if i == 0])
present = len([i for i in abs_list if i == 1])
print(f"Present: {present}")
print(f"Absent: {absent}")
