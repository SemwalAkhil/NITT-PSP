'''
PROBLEM STATEMENT: Merge two given string of characters
INPUT: String1 (S1), String2 (S2)
OUTPUT: Merged Sting (O)
Read S1, S2
L1 <- length(S1) - 1, L2 <- length(S2) - 1, counter <- 0, O <- ""
While L1 not -1 or L2 not -1 do
|   If L1 not -1 do
|   |   O += S1[counter]
|   |   L1 -= 1
|   If L2 not -1 do
|   |   O += S2[counter]
|   |   L2 -= 1
|   counter += 1
Write O
'''
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
    # print(string3)
    counter += 1

print(string3)