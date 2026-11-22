# 7. Write a program to extract institution and place names connected by 'of' using regex.
# Input: ("State Bank of India"), ("Just A Place")
# Output: State Bank | India |, Not found

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