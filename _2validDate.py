'''
check if a date is valid

constraints
-> feb has 29 days non leap 28 days
-> each month has different number of days
'''

def checkValid(date:int,month:int,year:int)->bool:
    '''
    input: date, month, year
    output: True/False
    '''
    if date < 1 or date > 31:
        return False          
    elif (month in (4,6,9,11)):
        if date == 30:
            return False
    elif (month == 2):
        if (year % 100 == 0):
            if (year % 400 == 0):
                if (date == 30):
                    return False
            elif (date == 29):
                return False
        elif (year % 4 == 0):
            if (date == 30):
                return False
        elif (date == 29):
            return False
    return True

if __name__ == "__main__":

    date = int(input("Enter date (DD): "))
    month = int(input("Enter month (MM): "))
    year = int(input("Enter year (YYYY): "))

    print("Valid Date" if checkValid(date,month,year) else "Invalid Date")