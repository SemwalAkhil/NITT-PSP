# hide some words/characters
string = input("Enter a phrase: ")
masked = string.replace("a", "_")
masked = masked.replace("e", "_")
masked = masked.replace("i", "_")
masked = masked.replace("o", "_")
masked = masked.replace("u", "_")
masked = masked.replace(" ", "_")
print(masked)
