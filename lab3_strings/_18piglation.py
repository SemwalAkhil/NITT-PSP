# 18. Write a program to convert words in a phrase to Pig Latin format with trailing 'M'.
# Input: ("Welcome to python"), ("hello world")
# Output: elcomeWM otM ythonpM, ellohM orldwM

string = input("Enter the phrase: ")
words = string.split()
for i in range(len(words)):
    words[i] = words[i][1:] + words[i][0] + 'M'
piglatin = " ".join(words)
print(piglatin)
