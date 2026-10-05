source = input("Enter train's starting station code: ")[:4].upper().ljust(4,"-") # 2-4 alphabet code
destination = input("Enter train's ending station code: ")[:4].upper().ljust(4,"-") # 2-4 alphabet code
print('''RE: Rajdhani Express
DE: Duronto Express
SE: Shatabdi Express
GE: Gatimaan Express
VE: Vande Bharat Express
HE: Humsafar Express
TE: Tejas Express
ME: Maharaja Express
SA: Samjhauta Express
MT: Metro Train
''')
ttype = input("Enter the train type: ")[:2].upper() 
zone = input("Enter the zone code: ")[:4].upper().ljust(4,"-") # 2-4 alphabet code
days = input("Enter weekly frequency: ")[:1]
serial = input("Enter 2 digit serial number: ")[:2]

print(source+destination+ttype+zone+days+serial)

