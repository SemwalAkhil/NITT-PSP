# 5. Write a program to read answer key and student responses from the user, evaluate quiz marks, and compute total scores.
# Input: ("A B B C A D A" 4 1 "A B B C A D A" 2 "A B A C B D A" 3 "B B B C A D C" 4 "A C B C A D A"), ("A B C" 2 1 "A B C" 2 "A A A")
# Output:
#   1: 7
#   2: 5
#   3: 5
#   4: 6

answer_key = tuple(input("Enter answer key: ").split())
num_students = int(input("Enter number of students: "))
students:dict[int, tuple[str,...]] = {}
for i in range(num_students):
    roll = int(input("Enter roll number: "))
    answers = tuple(input(f"Enter answers for roll {roll}: ").split())
    students[roll] = answers

marks:dict[int,int] = {
    i:0 for i in students.keys()
}
for roll,options in students.items():
    for option in range(len(options)):
        if option < len(answer_key) and options[option] == answer_key[option]:
            marks[roll] += 1

for student,mark in marks.items():
    print(f"{student}: {mark}")
