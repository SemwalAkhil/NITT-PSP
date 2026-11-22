# 16. Write a program to convert a decimal number to binary using loops.
# Input: (10), (7)
# Output: Binary is:  1010, Binary is:  111

num = int(input("Enter decimal: "))
bin = ""
while (num != 0):
    bin = ("1" if num % 2 else "0") + bin  
    num //= 2
print("Binary is: ",bin)