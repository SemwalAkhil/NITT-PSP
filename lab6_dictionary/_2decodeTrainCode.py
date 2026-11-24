# 2. Write a program to decode a train code into source, destination, type, zone, frequency, and serial number.
# Input: (MAS-SBC-SESR--701), (NDLSBCT-VENR--502)
# Output:
#   Run 1:
#   Source: MAS
#   Destination: SBC
#   Train type: SE
#   Zone: SR
#   Frequency: 7
#   Serial: 01
#   Run 2:
#   Source: NDLS
#   Destination: BCT
#   Train type: VE
#   Zone: NR
#   Frequency: 5
#   Serial: 02

train_code = input("Enter train code: ")
train_info = {"source":train_code[:4].strip("-"),"destination":train_code[4:8].strip("-"), "train type":train_code[8:10], "zone": train_code[10:14].strip("-"), "frequency": train_code[14:15], "serial": train_code[15:17]}
print("="*5 + "Train Information" + "="*5)
for key,value in train_info.items():
    print(f"{key.capitalize()}: {value}".center(27))
print("="*27)
