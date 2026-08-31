ram = int(input("Enter size of RAM(GB): "))
word = int(input("Word size (Bytes): "))
address = (ram * 2 ** 9) / word
bus = 0
while address > 1:
    address/=2
    bus += 1
print("Size of address bus: ",bus," bits")
