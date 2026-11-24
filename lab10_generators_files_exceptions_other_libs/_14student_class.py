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


s = Student("Rahul", 101)
s.add_sub(4, "O")
s.add_sub(3, "A")
print(s.name, "CGPA:", s.cgpa()) 
