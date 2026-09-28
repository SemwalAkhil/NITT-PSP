# Welcome => elcomeWX

string = input("Enter the phrase: ")
words = string.split()
for i in range(len(words)):
    words[i] = words[i][1:] + words[i][0] + 'M'
piglatin = " ".join(words)
print(piglatin)
