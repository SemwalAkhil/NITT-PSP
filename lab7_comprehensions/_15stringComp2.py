# toggleCase of a string
string = input("Enter string: ")
returnString = "".join([i.lower() if i.isupper() else i.upper() for i in string])
print(returnString)
