sent = input("Enter sentence: ").split()
print(" ".join(map(lambda x: "".join([chr(ord(char)+10) for char in x]), [word for word in sent])))

