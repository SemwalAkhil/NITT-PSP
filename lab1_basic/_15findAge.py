# 15. Write a program to calculate age in years, months, and days from date of birth.
# Input: (15-08-2000), (01-01-2010)
# Output: Age is : 26 years 3 months 7 days (depends on today's date), Age is : 16 years 10 months 21 days (depends on today's date)

"""
Read dob
diff<-dob-today
Print(diff.years, diff.months, diff.days)
"""
from datetime import date
dobDate, dobMonth, dobYear = input("Enter date (DD-MM-YYYY): ").split("-")
d = int(dobDate)
m = int(dobMonth)
y = int(dobYear)
today = date.today()

years = today.year - y
months = today.month - m
days = today.day - d

if days < 0:
    months -= 1
    # days in previous month
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

print("Age is : {} years {} months {} days".format(years, months, days))
