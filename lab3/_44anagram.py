# check if one string is permutation of another
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
if len(string1) == len(string2):
    if string1.split().sort() == string2.split().sort():
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")
