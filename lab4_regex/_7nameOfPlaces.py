'''
State Bank of India
High Court of Himachal Pradesh
High Court of HP
'''
import re

text = input("Enter institution: ")
match = re.search(r"([A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*)*)\s+of\s+([A-Z][A-Za-z]*(?:\s+[A-Z][A-Za-z]*)*)", text)

if match:
    for item in match.groups():
        print(item, end=" | ")
else:
    print("Not found")