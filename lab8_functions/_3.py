import re

def hashtagToWords(tag: str):
    words = re.findall(r"[A-Z][a-z]*", tag)
    return " ".join(words)

if __name__ == "__main__":
    tag = "#HelloWorldPython"
    print(hashtagToWords(tag))
