# 16. Write a program to decode roll number into degree level, department, year, and sequence number.
# Input: (205126009), (105125010)
# Output:
#   Type      : PG
#   Department: Computer Applications
#   Year      : 2026
#   Sequence  : 009

roll = input("Enter roll number: ")
if roll[:1] == "1":
    print("Type      : UG")
if roll[:1] == "2":
    print("Type      : PG")
if roll[1:3] == "05":
    print("Department: Computer Applications")
    if roll[3:5] == "01":
        print("Course    :MCA")
print(f"Year      : 20{roll[4:6]}")
print(f"Sequence  : {roll[6:]}")
