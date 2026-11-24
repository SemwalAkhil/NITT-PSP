"""Menu-driven program combining all 6 Lab 10 Python exercises."""

import re
import time
from functools import reduce

# --- Program 1: Authentication Decorator ---
db = {"admin": "1234", "rahul": "pass"}


def auth(func):
    def wrapper(user, pwd, *args):
        if db.get(user) == pwd:
            return func(*args)
        return "Access Denied"

    return wrapper


@auth
def add(a, b):
    return a + b


def run_authentication():
    """1. Demonstrate authentication decorator."""
    choice = input("Use sample test cases? (Y/n): ").strip().lower()
    if choice in ("", "y", "yes"):
        print('add("admin", "1234", 5, 10) ->', add("admin", "1234", 5, 10))
        print('add("admin", "0000", 5, 10) ->', add("admin", "0000", 5, 10))
    else:
        user = input("Username: ").strip()
        pwd = input("Password: ").strip()
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
            a = int(a) if a.is_integer() else a
            b = int(b) if b.is_integer() else b
        except ValueError:
            print("Invalid numbers.")
            return
        print("Result:", add(user, pwd, a, b))


# --- Program 2: Execution Time Decorator ---
def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        res = func(*args)
        print(f"Time: {time.perf_counter() - start:.6f}s")
        return res

    return wrapper


@timer
def total(n):
    return sum(range(n + 1))


def run_execution_time():
    """2. Measure execution time of sum(0..n) using @timer decorator."""
    raw = input("Enter n (press Enter for default 10): ").strip()
    if raw:
        try:
            n = int(raw)
            if n < 0:
                print("Please enter a non-negative integer.")
                return
        except ValueError:
            print("Invalid input. Using default 10.")
            n = 10
    else:
        n = 10

    print("Sum:", total(n))


# --- Program 3: Fibonacci Generator ---
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def run_fibonacci_generator():
    """3. Generate Fibonacci numbers using a generator."""
    raw = input("How many terms? (press Enter for default 7): ").strip()
    if raw:
        try:
            count = int(raw)
            if count < 0:
                print("Please enter a non-negative integer.")
                return
        except ValueError:
            print("Invalid input. Using default 7.")
            count = 7
    else:
        count = 7

    g = fib()
    print([next(g) for _ in range(count)])


# --- Program 4: Square Generator ---
def squares():
    n = 1
    while True:
        yield n * n
        n += 1


def run_square_generator():
    """4. Generate square numbers using a generator."""
    raw = input("How many terms? (press Enter for default 7): ").strip()
    if raw:
        try:
            count = int(raw)
            if count < 0:
                print("Please enter a non-negative integer.")
                return
        except ValueError:
            print("Invalid input. Using default 7.")
            count = 7
    else:
        count = 7

    g = squares()
    print([next(g) for _ in range(count)])


# --- Program 5: Student CGPA Class ---
class Student:
    grades = {"O": 10, "A": 9, "B": 8, "C": 7, "F": 0}

    def __init__(self, name, roll):
        self.name, self.roll = name, roll
        self.subs = []

    def add_sub(self, credits, grade):
        grade_key = grade.upper()
        if grade_key not in self.grades:
            raise ValueError(f"Unknown grade '{grade}'. Valid grades: {list(self.grades.keys())}")
        self.subs.append((credits, grade_key))

    def cgpa(self):
        pts = sum(c * self.grades[g] for c, g in self.subs)
        creds = sum(c for c, _ in self.subs)
        return round(pts / creds, 2) if creds else 0.0


def run_student_class():
    """5. Calculate student CGPA using the Student class."""
    choice = input("Use sample student (Rahul, Roll 101)? (Y/n): ").strip().lower()
    if choice in ("", "y", "yes"):
        s = Student("Rahul", 101)
        s.add_sub(4, "O")
        s.add_sub(3, "A")
        print(s.name, "CGPA:", s.cgpa())
    else:
        name = input("Student name: ").strip() or "Student"
        roll = input("Roll number: ").strip() or "1"
        s = Student(name, roll)
        try:
            num_subs = int(input("Number of subjects: "))
            for i in range(1, num_subs + 1):
                credits = int(input(f"  Subject {i} credits: "))
                grade = input(f"  Subject {i} grade (O/A/B/C/F): ").strip()
                s.add_sub(credits, grade)
        except ValueError as err:
            print("Invalid input:", err)
            return
        print(s.name, "CGPA:", s.cgpa())


# --- Program 6: Twitter Text Preprocessing ---
compose = lambda *fs: reduce(lambda f, g: lambda x: g(f(x)), fs)

lower = lambda t: t.lower()
no_url = lambda t: re.sub(r"http\S+", "", t)
no_tags = lambda t: re.sub(r"@\w+|#", "", t)
only_alpha = lambda t: re.sub(r"[^a-z\s]", "", t).strip()
no_stops = lambda t: [w for w in t.split() if w not in {"is", "the", "a", "at"}]

preprocess = compose(lower, no_url, no_tags, only_alpha, no_stops)


def run_twitter_preprocessing():
    """6. Preprocess a tweet using function composition."""
    default_tweet = "@dev Python is the best!! Check https://python.org "
    tweet = input(f"Enter a tweet (press Enter for default): ").strip() or default_tweet
    print("Preprocessed tokens:", preprocess(tweet))


def main():
    menu_options = {
        "1": ("Authentication Decorator", run_authentication),
        "2": ("Execution Time Decorator", run_execution_time),
        "3": ("Fibonacci Generator", run_fibonacci_generator),
        "4": ("Square Generator", run_square_generator),
        "5": ("Student CGPA Calculator", run_student_class),
        "6": ("Twitter Text Preprocessing", run_twitter_preprocessing),
    }

    while True:
        print("\n=== LAB 10: PYTHON PROGRAMS MENU ===")
        for key, (label, _) in menu_options.items():
            print(f"{key}. {label}")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ").strip()
        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice in menu_options:
            print()
            menu_options[choice][1]()
        else:
            print("Invalid choice. Please enter a number from 0 to 6.")


if __name__ == "__main__":
    main()