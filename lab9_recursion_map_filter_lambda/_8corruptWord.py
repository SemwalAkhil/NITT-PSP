# 8. Write a program to transform characters in words using map and lambda.
# Input: ("Hello World"), ("Python Lab")
# Output: Rovvy ay|vn, Z~ryx Vkl

sent = input("Enter sentence: ").split()
print(" ".join(map(lambda x: "".join([chr(ord(char)+10) for char in x]), [word for word in sent])))

