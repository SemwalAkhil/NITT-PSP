"""
8. List is date followed by list of absentees. 
ex: ['25-9-2026',51,101,67, '26-9-2026',51,101,68,59, '27-9-2026', 101,51, 28, 65]
find date wise absentees.
find for each roll no, how much class absent

INPUT: ['25-9-2026',51,101,67, '26-9-2026',51,101,68,59, '27-9-2026', 101,51, 28, 65]
OUTPUT: 
Absent students on 25-9-2026: 51 101 67 
Absent students on 26-9-2026: 51 101 68 59 
Absent students on 27-9-2026: 101 51 28 65 
Total classes absent by roll no 28: 1
Total classes absent by roll no 51: 3
Total classes absent by roll no 59: 1
Total classes absent by roll no 65: 1
Total classes absent by roll no 67: 1
Total classes absent by roll no 68: 1
Total classes absent by roll no 101: 3
"""

data = ['25-9-2026', 51, 101, 67, '26-9-2026', 51, 101, 68, 59,
        '27-9-2026', 101, 51, 28, 65]

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