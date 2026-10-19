"""
4. Convert a sentence to a list of words and sort it.
INPUT:  sentence(S)  "banana apple mango"
OUTPUT: ["apple", "banana", "mango"]
INPUT:  sentence(S)  "cat dog"
OUTPUT: ["cat", "dog"]
"""
sentence = input("Enter sentence: ")
words = sentence.split()
words.sort()
print(words)