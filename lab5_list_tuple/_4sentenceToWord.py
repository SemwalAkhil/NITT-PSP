# 4. Write a program to split a sentence into words and print them in alphabetical order.
# Input: ("hello world python"), ("the quick brown fox")
# Output: ['hello', 'python', 'world'], ['brown', 'fox', 'quick', 'the']

sentence = input("Enter sentence: ")
words = sentence.split()
words.sort()
print(words)