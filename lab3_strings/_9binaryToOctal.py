string = input("Enter binary: ").strip().strip(".").split(".")

left = string[0]
right = ""
if len(string) == 2:
    right = string[1]

octal = ""

if len(left) % 3 == 1:
    left = "00" + left
if len(left) % 3 == 2:
    left = "0" + left

for i in range(len(left)-1,-1,-3):
    temp = left[i-2:i+1]
    temp = 2**2 * int(temp[0]) + 2**1 * int(temp[1]) + 2**0 * int(temp[2])
    octal = str(temp) + octal

if right != "":
    octal += "."
    if len(right) % 3 == 1:
        right = right + "00" 
    if len(right) % 3 == 2:
        right = right + "0"

    for i in range(0,len(right),3):
        temp = right[i:i+3]
        temp = 2**2 * int(temp[0]) + 2**1 * int(temp[1]) + 2**0 * int(temp[2])
        octal = octal + str(temp)

print("Octal representation is: ",octal)
