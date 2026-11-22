# 4. Write a program to decode train codes from a file, validate length by raising ValueError, and handle errors.
# Input: None (data defined in the script)
# Output:
#   Decoded MAS-SBC-SERSR-701: {'source': 'MAS', 'destination': 'SBC', 'type': 'SE', 'zone': 'RSR', 'frequency': '7', 'serial': '01'}
#   Error decoding 'SHORT123': Invalid code length 8
#   Decoded NDLSBCT-VE-NR-502: {'source': 'NDLS', 'destination': 'BCT', 'type': 'VE', 'zone': 'NR', 'frequency': '5', 'serial': '02'}

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

filename = "train_codes.txt"
with open(filename, "w") as f:
    f.write("MAS-SBC-SERSR-701\nSHORT123\nNDLSBCT-VE-NR-502\n")

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
