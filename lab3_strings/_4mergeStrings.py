string1 = input("Enter string 1: ")
len1 = len(string1) - 1
string2 = input("Enter string 2: ")
len2 = len(string2) - 1
string3 = ""
counter = 0
while len1 != -1 or len2 != -1:
    if len1 != -1:
        string3 += string1[counter]
        len1 -= 1
    if len2 != -1:
        string3 += string2[counter]
        len2 -= 1
    counter += 1

print(string3)