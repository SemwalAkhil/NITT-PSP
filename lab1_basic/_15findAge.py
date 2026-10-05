"""
Read dob
diff<-dob-today
Print(diff.years, diff.months, diff.days)
"""
from datetime import date
from dateutil.relativedelta import relativedelta
dobDate, dobMonth, dobYear = input("Enter date (DD-MM-YYYY): ").split("-")
dob = date(int(dobYear),int(dobMonth),int(dobDate))
today = date.today()
diff = relativedelta(today,dob)
print("Age is : {} years {} months {} days".format(diff.years,diff.months,diff.days))
