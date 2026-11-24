# 1. Write a program to decode a 9-digit roll number into level, department, year, and sequence.
# Input: (205126009), (101124015)
# Output:
#   Run 1:
#   Level: PG
#   Department: Computer Applications
#   Year of Admission: 2026
#   Sequence Number:  009
#   Run 2:
#   Level: UG
#   Department: Architecture
#   Year of Admission: 2024
#   Sequence Number:  015

R = input("Enter a nine digit roll number: ")

print("Level: ",end="")
p1 = R[:1]
if p1 == "1":
    print("UG")
elif p1 == "2":
    print("PG")
elif p1 == "3" or p1 == "4":
    print("Ph.D.")
else:
    print("Unknown")

print("Department: ",end="")
p2 = R[1:3]
if p2 == "01":
    print("Architecture")
elif p2 == "03":
    print("Civil Engineering")
elif p2 == "05":
    print("Computer Applications")
else:
    print("Unknown")

print("Year of Admission: 20" + R[4:6])

print("Sequence Number: ",R[6:])