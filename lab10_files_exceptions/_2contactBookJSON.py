# 2. Write a program to store and load a contact book using JSON format with file and decode error handling.
# Input: (contacts.json 2 Akhil akhil@example.com 9876543210 Rahul rahul@example.com 9123456780), (book.json 1 Alice alice@test.com 11111)
# Output:
#   Loaded contacts:
#   Name: Akhil, Email: akhil@example.com, Phone: 9876543210
#   Name: Rahul, Email: rahul@example.com, Phone: 9123456780

import json

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
