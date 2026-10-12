# hide some words/characters
string = input("Enter a phrase: ")
masked = "".join(["_" if i.lower() in "aeiou" else i for i in string ]) 
print(masked)
