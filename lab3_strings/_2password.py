'''
    Create password from details
    Blood Group -> 1 letter
    Month -> first 3 letter in upper case
    DOB -> 2 digit date
    Phone number -> last three digit
'''
'''
PROBLEM STATEMENT: Given details of student generate his password
INPUT: Blood Group (B), DOB (D), Phone Number (P)
OUTPUT: Output password
Read B, D, P
Write B[:1] + DOB.month[:3].upper + DOB.day + P[-3:]
'''
import datetime


blood_group = input("Enter your blood group: ")[:1]
datestring = input("Enter your date of birth (DD/MM/YYYY): ")
date = datetime.datetime.strptime(datestring,"%d/%m/%Y")

phone_number = input("Enter phone number: ")[-3:]

print(blood_group + date.strftime("%B")[:3].upper() +str(date.day)+phone_number)