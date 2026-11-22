# 5. Write a program to find the start and end index of a substring within a sentence.
# Input: ("hello world" world), ("python programming" gram)
# Output:
#   Start:  6 
#   End:  11

string1 = input("Enter sentence: ")
string2 = input("Enter substring: ")
index = string1.find(string2)
print("Start: ",index,"\nEnd: ",index+len(string2))