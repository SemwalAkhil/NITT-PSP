string1 = input("Enter string1: ")
string2 = input("Enter string2: ")

counter = 0
subsLen = 0

while counter != len(string1) and counter != len(string2):
    if string1[counter] == string2[counter]:
        subsLen += 1
    else:
        break
    counter += 1

print("Largest common prefix: ",string1[:subsLen])
