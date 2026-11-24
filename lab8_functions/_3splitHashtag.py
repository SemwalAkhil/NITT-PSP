# 3. Write a function to split a camelCase or PascalCase hashtag into words using regular expressions.
# Input: ("#HelloWorldPython"), ("#PythonProgramming")
# Output: Hello World Python, Python Programming

import re

def hashtagToWords(tag: str):
    words = re.findall(r"[A-Z][a-z]*", tag)
    return " ".join(words)

if __name__ == "__main__":
    tag = input("Enter hashtag: ")
    print(hashtagToWords(tag))
