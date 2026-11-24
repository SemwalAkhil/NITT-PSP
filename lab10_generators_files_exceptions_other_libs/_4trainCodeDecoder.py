# 4. Write a program to decode train codes from a file and log error details for invalid lines.
# Input: (1), (2)
# Output:
#   Run 1:
#   Decoded MAS-SBC-SESR--701: {'source': 'MAS', 'destination': 'SBC', 'type': 'SE', 'zone': 'SR', 'frequency': '7', 'serial': '01'}
#   Decoded NDLSBCT-VENR--502: {'source': 'NDLS', 'destination': 'BCT', 'type': 'VE', 'zone': 'NR', 'frequency': '5', 'serial': '02'}
#   Decoded HWH-MAS-RSER--303: {'source': 'HWH', 'destination': 'MAS', 'type': 'RS', 'zone': 'ER', 'frequency': '3', 'serial': '03'}
#   Decoded CSTMNGP-CRCR--604: {'source': 'CSTM', 'destination': 'NGP', 'type': 'CR', 'zone': 'CR', 'frequency': '6', 'serial': '04'}
#   Decoded SBC-UBL-SWSWR-705: {'source': 'SBC', 'destination': 'UBL', 'type': 'SW', 'zone': 'SWR', 'frequency': '7', 'serial': '05'}
#   Run 2:
#   Decoded MAS-SBC-SESR--701: {'source': 'MAS', 'destination': 'SBC', 'type': 'SE', 'zone': 'SR', 'frequency': '7', 'serial': '01'}
#   Error decoding 'SHORT123': Invalid code length 8
#   Decoded NDLSBCT-VENR--502: {'source': 'NDLS', 'destination': 'BCT', 'type': 'VE', 'zone': 'NR', 'frequency': '5', 'serial': '02'}
#   Error decoding 'TOOLONGLINETRAINCODE12345': Invalid code length 25
#   Error decoding 'BAD': Invalid code length 3
#   Decoded SBC-UBL-SWSWR-705: {'source': 'SBC', 'destination': 'UBL', 'type': 'SW', 'zone': 'SWR', 'frequency': '7', 'serial': '05'}

import os

def decode_train_code(code: str):
    if len(code) != 17:
        raise ValueError(f"Invalid code length {len(code)}")
    return {
        "source": code[:4].strip("-"),
        "destination": code[4:8].strip("-"),
        "type": code[8:10],
        "zone": code[10:14].strip("-"),
        "frequency": code[14:15],
        "serial": code[15:17]
    }

sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data")
choice = input("Use sample data? (1 = clean, 2 = with errors, 0 = type my own): ").strip()

if choice == "1":
    filename = os.path.join(sample_dir, "train_codes_clean.txt")
elif choice == "2":
    filename = os.path.join(sample_dir, "train_codes_errors.txt")
else:
    filename = input("Enter train codes filename: ")
    n = int(input("Enter number of train codes: "))
    with open(filename, "w") as f:
        for i in range(n):
            f.write(input("Enter train code: ") + "\n")

try:
    with open(filename, "r") as f:
        for line in f:
            code = line.strip()
            if not code:
                continue
            try:
                info = decode_train_code(code)
                print(f"Decoded {code}: {info}")
            except ValueError as e:
                print(f"Error decoding '{code}': {e}")
except FileNotFoundError:
    print(f"File {filename} not found")
