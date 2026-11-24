# 2. Write a program to store contacts in a JSON file, handle JSONDecodeError, and display saved contacts.
# Input: (1), (2)
# Output:
#   Run 1:
#   Loaded contacts:
#   Name: Akhil, Email: akhil@example.com, Phone: 9876543210
#   Name: Rahul, Email: rahul@example.com, Phone: 9123456780
#   Name: Priya, Email: priya@example.com, Phone: 9988776655
#   Name: Ankit, Email: ankit@example.com, Phone: 9811223344
#   Name: Sneha, Email: sneha@example.com, Phone: 9744556677
#   Run 2:
#   Corrupt JSON file E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\contacts_corrupt.json

import json
import os

sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data")
choice = input("Use sample data? (1 = clean, 2 = with errors, 0 = type my own): ").strip()

if choice == "1":
    filename = os.path.join(sample_dir, "contacts_clean.json")
elif choice == "2":
    filename = os.path.join(sample_dir, "contacts_corrupt.json")
else:
    filename = input("Enter JSON filename: ")
    n = int(input("Enter number of contacts: "))
    contacts = {}
    for i in range(n):
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        contacts[name] = {"email": email, "phone": phone}

    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)

try:
    with open(filename, "r") as f:
        data = json.load(f)
        print("Loaded contacts:")
        for name, info in data.items():
            print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}")
except FileNotFoundError:
    print(f"File {filename} not found")
except json.JSONDecodeError:
    print(f"Corrupt JSON file {filename}")
