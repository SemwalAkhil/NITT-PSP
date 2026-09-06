'''

PROBLEM STATEMENT: Encrypt/Decrypt a given string of characters 
INPUT: String (S)
OUTPUT: Encrypted/Decrypted String
Read S
For i <- 0 to len(S) do
|   ascii <- ord(S[i])
|   S <- S.replace(S[i], Z - ascii + A) or S.replace(S[i], z - ascii + a)
Write S
'''
def encrypt(string:str)->str:
    for i in range(len(string)):
        ascii = ord(string[i])
        string = string.replace(string[i],chr(ord('Z') - ascii + ord('A')) if ascii <= ord('Z') else  chr(ord('z') - ascii + ord('a')) )
    return string

if __name__ == "__main__":
    # string = input("Enter a string: ")
    string = "akhil"
    print("Original String: ",string)
    encrypted = encrypt(string)
    print("Encrypted String: ", encrypted)
    decrypted = encrypt(encrypted)
    print("Decryption: ",decrypted)