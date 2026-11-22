# 4. Write a program to corrupt a string by shifting digits and toggling case using comprehension.
# Input: (Abc123Xyz), (Hello1)
# Output: aBC;<=xYZ, hELLO;

print("".join(chr(ord(char)+10) if char.isdigit() else (char.lower() if char.isupper() else char.upper()) for char in input("Enter a string: ")))
