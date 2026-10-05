from datetime import date
from dateutil.relativedelta import relativedelta

num = int(input("Enter number of students: "))
dob:dict[str:str] = {}
age:dict[str:str] = {}
for i in range(num):
    name = input("Enter student name: ")
    dob[name] = input("Enter dob (DD/MM/YYYY): ")[:10]

print("You Entered".center(25,"="))
for name,day in dob.items():
    diff = relativedelta(date.today(),date(int(day[6:]),int(day[3:5]),int(day[:2])))
    age[name] = f"{diff.years} years, {diff.months} months, {diff.days} days"

print("Ages".center(25,"="))
for name,diff in age.items():
    print(f"{name}: {diff}")
    