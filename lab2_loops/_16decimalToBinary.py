num = int(input("Enter decimal: "))
bin = ""
while (num != 0):
    bin = ("1" if num % 2 else "0") + bin  
    num //= 2
print("Binary is: ",bin)