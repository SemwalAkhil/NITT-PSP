# toggleCase of a string

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
