# 21. Write a program to toggle the case of each character in a given string.
# Input: ("Hello World"), ("PyThOn 123")
# Output: hELLO wORLD, pYtHoN 123

string = input("Enter string: ")
returnString = ""
for i in range(len(string)):
    if string[i].islower():
        returnString += string[i].upper()
    elif string[i].isupper():
        returnString += string[i].lower()
    else:
        returnString += string[i]
print(returnString)
