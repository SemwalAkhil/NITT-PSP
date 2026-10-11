import re
gst_num = input("Enter GST number: ")
match = re.match(r"([0-9]{2})([A-Z0-9]{10})([0-9])Z([0-9])",gst_num)
if match:
    print("Valid GST number")
    print(f"State Code: {match.group(1)}")
    print(f"PAN: {match.group(2)}")
    print(f"Number of registrations on PAN: {match.group(3)}")
    print(f"Checksum: {match.group(4)}")
else:
    print("Invalid GST number")