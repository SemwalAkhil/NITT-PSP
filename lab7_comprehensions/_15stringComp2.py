# 15. Write a program to toggle the case of each character in a string using comprehension.
# Input: ("Hello World"), ("Python 123")
# Output: hELLO wORLD, pYTHON 123

string = input("Enter string: ")
returnString = "".join([i.lower() if i.isupper() else i.upper() for i in string])
print(returnString)
