# 8. Write a program to calculate hard disk capacity in bytes given its size in gigabytes.
# Input: (10), (2)
# Output: HDD can hold:  10737418240  Bytes, HDD can hold:  2147483648  Bytes

size = int(input("Enter size of hard disk(GB): "))
print("HDD can hold: ",size * 2 ** 30," Bytes")