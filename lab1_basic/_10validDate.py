'''
Read D,M,Y
If D < 1 or D > 31 or M < 1 or M > 12 do
    Print(Invalid)
Else If M in 4,6,9,11 do
    If 0 < D < 31 do
        Print(Valid)
    Else do
        Print(Invalid)
Else If M = 2 do
    If Y is leap do
        If 0 < D < 30 do
            Print(Valid)
        Else do
            Print(Invalid)
    Else do
        If 0 < D < 29 do
            Print(Valid)
        Else do
            Print(Invalid)
Else do
    Print(Invalid)
'''

date = int(input("Enter date (DD): "))
month = int(input("Enter month (MM): "))
year = int(input("Enter year (YYYY): "))

if date < 1 or date > 31 or month < 1 or month > 12:
    print("Invalid Date")
elif (month in (4,6,9,11)):
    if 0 < date < 31:
        print("Valid Date")
    else:
        print("Invalid Date") 
elif (month == 2):
    if ((year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)):
        if 0 < date < 30:
            print("Valid Date")
        else:
            print("Invalid Date")
    else:
        if 0 < date < 29:
            print("Valid Date") 
        else:
            print("Invalid Date")
else:
    print("Valid Date")

