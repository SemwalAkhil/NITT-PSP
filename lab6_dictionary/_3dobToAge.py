# 3. Write a program to calculate age in years, months, and days for multiple students using a dictionary.
# Input: (1 Akhil 15/08/2000), (1 John 01/01/2010)
# Output: Akhil: 26 years, 3 months, 7 days (depends on today's date), John: 16 years, 10 months, 21 days (depends on today's date)

from datetime import date

num = int(input("Enter number of students: "))
dob:dict[str,str] = {}
age:dict[str,str] = {}
for i in range(num):
    name = input("Enter student name: ")
    dob[name] = input("Enter dob (DD/MM/YYYY): ")[:10]

today = date.today()

print("You Entered".center(25,"="))
for name,day in dob.items():
    d = int(day[:2])
    m = int(day[3:5])
    y = int(day[6:])

    years = today.year - y
    months = today.month - m
    days = today.day - d

    if days < 0:
        months -= 1
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        if prev_month in (1, 3, 5, 7, 8, 10, 12):
            days += 31
        elif prev_month in (4, 6, 9, 11):
            days += 30
        elif (prev_year % 400 == 0) or (prev_year % 100 != 0 and prev_year % 4 == 0):
            days += 29
        else:
            days += 28

    if months < 0:
        years -= 1
        months += 12

    age[name] = f"{years} years, {months} months, {days} days"

print("Ages".center(25,"="))
for name,diff in age.items():
    print(f"{name}: {diff}")
