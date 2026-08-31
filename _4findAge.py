import datetime
from _2validDate import checkValid
def getValidDate()->tuple[int]:
    year = int(input("Enter Year (YYYY): "))
    while True:
        month = int(input("Enter Month (MM): "))
        if month in range(1,13):
            break
        print("Enter valid month")
    while True:
        date = int(input("Enter Date (DD): "))
        if checkValid(date,month,year):
            break
        print("Enter valid date")
    return (date,month,year)
if __name__ == "__main__":
    dobDate, dobMonth, dobYear = getValidDate()
    dob = datetime.date(dobYear,dobMonth,dobDate)
    today = datetime.date.today()
    print("Age is : ",int((today - dob).days/365))
