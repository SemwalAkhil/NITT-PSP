def addContact(book: dict, name: str, email: str, phone: str):
    book[name] = {"email": email, "phone": phone}

def viewAll(book: dict):
    for name, info in book.items():
        print(f"Name: {name}, Email: {info['email']}, Phone: {info['phone']}")

def searchContact(book: dict, name: str):
    if name in book:
        info = book[name]
        print(f"Found - Name: {name}, Email: {info['email']}, Phone: {info['phone']}")
    else:
        print("Contact not found")

def menu():
    book = {}
    while True:
        print("\n1. Add Contact\n2. View All\n3. Search\n4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter contact no.: ")
            addContact(book, name, email, phone)
        elif choice == "2":
            viewAll(book)
        elif choice == "3":
            name = input("Enter name to search: ")
            searchContact(book, name)
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
