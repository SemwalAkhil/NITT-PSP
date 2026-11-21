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
