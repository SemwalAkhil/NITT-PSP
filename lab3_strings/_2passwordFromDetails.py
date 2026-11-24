# 2. Write a program to generate a password from blood group, birth date, and phone number.
# Input: (O+ 15/08/2000 9876543210), (A+ 01/01/2005 9123456789)
# Output: OAUG15210, AJAN1789

import datetime


blood_group = input("Enter your blood group: ")[:1]
datestring = input("Enter your date of birth (DD/MM/YYYY): ")
date = datetime.datetime.strptime(datestring,"%d/%m/%Y")

phone_number = input("Enter phone number: ")[-3:]

print(blood_group + date.strftime("%B")[:3].upper() +str(date.day)+phone_number)