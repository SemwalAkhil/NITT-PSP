'''
PROBLEM STATEMENT: Given to strings find the largest common part from the start of the strings
INPUT: String1 (S1), String2 (S2)
OUTPUT: Common String (O)
Read S1, S2
O <- ''
Counter <- 0
Substring_Length <- 0
While counter is not equal to length of S1 or S2 do
|   If S1[counter] = S2[counter]
|   | Substring_Length <- Substring_Length + 1
|   Counter <- Counter + 1
O <- S1[0:Substring_Length]
Write O 
'''
string1 = input("Enter string1: ")
string2 = input("Enter string2: ")

counter = 0
subsLen = 0

while counter != len(string1) and counter != len(string2):
    if string1[counter] == string2[counter]:
        subsLen += 1
    counter += 1

print("Largest common prefix: ",string1[:subsLen])