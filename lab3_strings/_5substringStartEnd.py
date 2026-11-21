string1 = input("Enter sentence: ")
string2 = input("Enter substring: ")
index = string1.find(string2)
print("Start: ",index,"\nEnd: ",index+len(string2))