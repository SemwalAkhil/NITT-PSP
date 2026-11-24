# 8. Write a program to record absent roll numbers per date and compute total absences per student.
# Input: (3 25-9-2026 "51 101 67" 26-9-2026 "51 101 68 59" 27-9-2026 "101 51 28 65"), (2 01-10-2026 "10 20" 02-10-2026 "20 30")
# Output:
#   Run 1:
#   Absent students on 25-9-2026: 51 101 67 
#   Absent students on 26-9-2026: 51 101 68 59 
#   Total classes absent by roll no 51: 3
#   Total classes absent by roll no 101: 3
#   Run 2:
#   Absent students on 01-10-2026: 10 20 
#   Absent students on 02-10-2026: 20 30 
#   Total classes absent by roll no 10: 1
#   Total classes absent by roll no 20: 2
#   Total classes absent by roll no 30: 1

n = int(input("Enter number of days: "))
data = []
for i in range(n):
    d = input("Enter date (DD-MM-YYYY): ")
    data.append(d)
    abs_rolls = input("Enter absent roll numbers: ").split()
    for r in abs_rolls:
        data.append(int(r))

rolls = []

for item in data:
    if isinstance(item, str):
        print("\nAbsent students on", item, end=": ")
    else:
        print(item, end=" ")
        if item not in rolls:
            rolls.append(item)

print("\n")

rolls.sort()

for roll in rolls:
    count = 0
    for item in data:
        if item == roll:
            count += 1
    print("Total classes absent by roll no", str(roll) + ":", count)
