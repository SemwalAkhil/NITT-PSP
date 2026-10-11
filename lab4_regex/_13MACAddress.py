import re
mac = input("Enter MAC address: ").upper()
match = re.findall(r"[0-9A-F]{2}",mac)
if match:
    print(f"Vendor OUI: {':'.join(match[:3])}")
    print(f"Device ID: {':'.join(match[-3:])}")
else:
    print("Invalid MAC")