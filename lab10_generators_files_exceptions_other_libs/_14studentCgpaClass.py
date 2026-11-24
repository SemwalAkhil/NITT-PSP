# 14. Write a Student class to track courses, credits, and grades and compute CGPA.
# Input: (Rahul 101 2 4 O 3 A), (Alice 102 1 4 B)
# Output: Rahul CGPA: 9.57, Alice CGPA: 8.0

class Student:
    grades = {"O": 10, "A": 9, "B": 8, "C": 7, "F": 0}

    def __init__(self, name, roll):
        self.name, self.roll = name, roll
        self.subs = []

    def add_sub(self, credits, grade):
        self.subs.append((credits, grade.upper()))

    def cgpa(self):
        pts = sum(c * self.grades[g] for c, g in self.subs)
        creds = sum(c for c, _ in self.subs)
        return round(pts / creds, 2) if creds else 0.0

name = input("Enter name: ")
roll = int(input("Enter roll number: "))
s = Student(name, roll)
n = int(input("Enter number of subjects: "))
for _ in range(n):
    c = int(input("Enter credits: "))
    g = input("Enter grade: ")
    s.add_sub(c, g)
print(s.name, "CGPA:", s.cgpa())
