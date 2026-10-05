'''
PROBLEM STATEMENT: Given a binary string convert to octal
INPUT: Binary (B)
OUTPUT: Octal (O)
Read B
O <- Octal(Integer(Binary,base=2))[2:]
Write O
'''

string = input("Enter binary: ")
print(f"Octal of {string} is: {oct(int(string,2))[2:]}")


'''
PROBLEM STATEMENT: Given a octal string convert to binary
INPUT: Octal (O)
OUTPUT: Binary (B)
Read O
O <- Binary(Integer(Octal,base=8))[2:]
Write O
'''
string = input("Enter octa: ")
print(f"Binary of {string} is: {bin(int(string,8))[2:]}")