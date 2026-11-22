# 5. Write a program to evaluate student quiz answers against an answer key and compute total scores using dictionaries.
# Input: None (data defined in the script)
# Output:
#   1: 7
#   2: 5
#   3: 5
#   4: 6

answer_key:tuple[str,...] = ('A','B','B','C','A','D','A')
students:dict[int, tuple[str,...]] = {
    1: ("A","B","B","C","A","D","A"),  # Perfect score
    2: ("A","B","A","C","B","D","A"),  # Missed Q3 and Q5
    3: ("B","B","B","C","A","D","C"),  # Missed Q1 and Q7
    4: ("A","C","B","C","A","D","A"),  # Missed Q2
}
marks:dict[int,int] = {
    i:0 for i in range(1,len(students.items())+1)
}
for roll,options in students.items():
    for option in range(len(options)):
        if options[option] == answer_key[option]:
            marks[roll] += 1

for student,mark in marks.items():
    print(f"{student}: {mark}")