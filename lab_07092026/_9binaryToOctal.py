string = input("Enter binary: ")
print(f"Octal of {string} is: {oct(int(string,2))[2:]}")

string = input("Enter octa: ")
print(f"Binary of {string} is: {bin(int(string,8))[2:]}")