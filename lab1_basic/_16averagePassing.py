# 16. Write a program to calculate the average of passing marks (>= 40) for a given list of students.
# Input: ("35 45 60 20 80"), ("30 25 39")
# Output: Average of passing marks:  61.666666666666664, No passing students

marks = input("Enter marks of students: ").split()
total = 0
count = 0
for m in marks:
    val = float(m)
    if val >= 40:
        total += val
        count += 1

if count > 0:
    print("Average of passing marks: ", total / count)
else:
    print("No passing students")
