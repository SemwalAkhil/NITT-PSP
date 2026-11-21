import datetime


blood_group = input("Enter your blood group: ")[:1]
datestring = input("Enter your date of birth (DD/MM/YYYY): ")
date = datetime.datetime.strptime(datestring,"%d/%m/%Y")

phone_number = input("Enter phone number: ")[-3:]

print(blood_group + date.strftime("%B")[:3].upper() +str(date.day)+phone_number)