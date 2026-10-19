'''
PROBLEM STATEMENT: Given a string and a substring find the starting and the end index of the substring
INPUT:  String (S1), Substring(S2)
OUTPUT: Index (I1), Index + Length (I2)
Read S1, S2
I1 <- S1.find(S2)
Write I1, I1 + len(S2)
'''
string1 = input("Enter sentence: ")
string2 = input("Enter substring: ")
index = string1.find(string2)
print("Start: ",index,"\nEnd: ",index+len(string2))