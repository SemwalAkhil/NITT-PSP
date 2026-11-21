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
