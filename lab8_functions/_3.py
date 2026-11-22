# 3. Write a function to split a camelCase or PascalCase hashtag into words using regular expressions.
# Input: tag="#HelloWorldPython"
# Output: Hello World Python

import re

def hashtagToWords(tag: str):
    words = re.findall(r"[A-Z][a-z]*", tag)
    return " ".join(words)

if __name__ == "__main__":
    tag = "#HelloWorldPython"
    print(hashtagToWords(tag))
