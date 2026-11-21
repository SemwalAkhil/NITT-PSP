import json

filename = "contacts.json"
contacts = {
    "Akhil": {"email": "akhil@example.com", "phone": "9876543210"},
    "Rahul": {"email": "rahul@example.com", "phone": "9123456780"}
}

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
