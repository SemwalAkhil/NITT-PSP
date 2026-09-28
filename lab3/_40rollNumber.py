# 205126009
roll = input("Enter roll number: ")
if roll[:1] == "1":
    print("Type      : UG")
if roll[:1] == "2":
    print("Type      : PG")
if roll[1:3] == "05":
    print("Department: Computer Applications")
    if roll[3:4] == "01":
        print("Course    :MCA")
print(f"Year      : 20{roll[4:6]}")
print(f"Sequence  : {roll[6:]}")
