# Mr. R. M. Nandha, Dr. (Mrs.)V. Priyadarshini, Ram Kumar Verma
import re
name = input("Enter name: ")
match = re.search(r"?(Dr\.)\s*?(Mr\.|Mrs\.|Ms\.)\s*(\w+)", name)
if match.group(1):
    print("Dr.")
if match.group(2):
    print("Mr./Mrs./Ms.: ")
print('Name: ', match.group(3))
