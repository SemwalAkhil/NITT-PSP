print("".join(chr(ord(char)+10) if char.isdigit() else (char.lower() if char.isupper() else char.upper()) for char in input("Enter a string: ")))
