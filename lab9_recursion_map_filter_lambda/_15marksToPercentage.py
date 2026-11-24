# 15. Write a program to compute student percentages from subject marks using map and lambda.
# Input: (3 1 "60 80 30 70" 2 "90 60 50 40" 3 "10 50 30 40"), (1 101 "80 90")
# Output:
#   Run 1:
#   1:60.0%
#   2:60.0%
#   3:32.5%
#   Run 2:
#   101:85.0%

n = int(input("Enter number of students: "))
marks = {}
for i in range(n):
    roll = int(input("Enter roll number: "))
    m_list = [int(x) for x in input(f"Enter marks for roll {roll}: ").split()]
    marks[roll] = m_list

print("\n".join(map(lambda x: f"{x}:{sum(marks[x])/len(marks[x])}%",marks.keys())))
