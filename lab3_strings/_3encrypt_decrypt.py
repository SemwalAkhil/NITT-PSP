# 3. Write a program to encrypt and decrypt a string using the Atbash cipher.
# Input: ("Hello World!"), ("Attack at Dawn")
# Output: Encrypted String:  Svool Dliow!, Encrypted String:  Zggzxp zg Wzdm

def encrypt(string):
    res = ""
    for char in string:
        if 'a' <= char <= 'z':
            res += chr(ord('z') - ord(char) + ord('a'))
        elif 'A' <= char <= 'Z':
            res += chr(ord('Z') - ord(char) + ord('A'))
        else:
            res += char
    return res

string = input("Enter a string: ")
print("Original String: ",string)
encrypted = encrypt(string)
print("Encrypted String: ", encrypted)
decrypted = encrypt(encrypted)
print("Decryption: ",decrypted)
