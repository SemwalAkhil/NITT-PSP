# 5. Write a program to find the start and end index of a substring in a given sentence.
# Input: ("hello world" world), ("python programming" gram)
# Output:
#   Run 1:
#   Start:  6 
#   End:  11
#   Run 2:
#   Start:  10 
#   End:  14

string1 = input("Enter sentence: ")
string2 = input("Enter substring: ")
index = string1.find(string2)
print("Start: ",index,"\nEnd: ",index+len(string2))