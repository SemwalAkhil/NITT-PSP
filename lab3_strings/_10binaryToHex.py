# 10. Write a program to convert a binary string (including fractional part) to hexadecimal.
# Input: (1101.101), (1111)
# Output: Hex representation is:  D.A, Hex representation is:  F

string = input("Enter binary: ").strip().strip(".").split(".")

left = string[0]
right = ""
if len(string) == 2:
    right = string[1]

Hex = ""
hex_chars = "0123456789ABCDEF"

if len(left) % 4 == 1:
    left = "000" + left
if len(left) % 4 == 2:
    left = "00" + left
if len(left) % 4 == 3:
    left = "0" + left

for i in range(len(left) - 1, -1, -4):
    temp = left[i-3:i+1]
    val = 2**3 * int(temp[0]) + 2**2 * int(temp[1]) + 2**1 * int(temp[2]) + 2**0 * int(temp[3])
    Hex = hex_chars[val] + Hex

if right != "":
    Hex += "."
    if len(right) % 4 == 1:
        right = right + "000" 
    if len(right) % 4 == 2:
        right = right + "00"
    if len(right) % 4 == 3:
        right = right + "0"

    for i in range(0, len(right), 4):
        temp = right[i:i+4]
        val = 2**3 * int(temp[0]) + 2**2 * int(temp[1]) + 2**1 * int(temp[2]) + 2**0 * int(temp[3])
        Hex = Hex + hex_chars[val]

print("Hex representation is: ", Hex)