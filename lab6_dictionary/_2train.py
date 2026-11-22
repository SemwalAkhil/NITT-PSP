# 2. Write a program to decode a train identification code into its constituent attributes using a dictionary.
# Input: (MAS-SBC-SESR--701), (NDLSBCT-VENR--502)
# Output:
#   Source: MAS
#   Destination: SBC
#   Train type: SE
#   Zone: SR
#   Frequency: 7
#   Serial: 01

train_code = input("Enter train code: ")
train_info = {"source":train_code[:4].strip("-"),"destination":train_code[4:8].strip("-"), "train type":train_code[8:10], "zone": train_code[10:14].strip("-"), "frequency": train_code[14:15], "serial": train_code[15:17]}
print("="*5 + "Train Information" + "="*5)
for key,value in train_info.items():
    print(f"{key.capitalize()}: {value}".center(27))
print("="*27)
