# 4. Write a program to build an inverted index from text pages and rank pages by matching query terms.
# Input: (2 "python is fun" "python lab programming" "python"), (1 "hello world" "world")
# Output:
#   Run 1:
#   ============= TOP 3 Pages ============= 
#   Page: 1 Matches: 1
#   Page: 2 Matches: 1
#   Page: 0 Matches: 0
#   Run 2:
#   ============= TOP 3 Pages ============= 
#   Page: 1 Matches: 1
#   Page: 0 Matches: 0
#   Page: 0 Matches: 0

import re

n = int(input("Enter number of pages: "))
text:dict[int,str] = {}
for i in range(1, n + 1):
    text[i] = input(f"Enter text for page {i}: ")

index = {}

for key,value in text.items():
    words = re.findall(r"\b[\w-]+\b",value.lower())
    for word in words:
        if word not in index:
            index[word] = (key,)
        elif key not in index[word]:
            index[word] += (key,)

for key,value in index.items():
    print(f"{key} : {value}")

phrase:list[str] = input("Enter a phrase: ").lower().split()
refcount:dict[int,int] = {i+1:0 for i in range(len(text.keys()))}

for word in phrase:
    for page_num in index.get(word,()):
        refcount[page_num] += 1

print(refcount)

high1 = (0,0)
high2 = (0,0)
high3 = (0,0)

for page,refs in refcount.items():
    if refs > high1[1]:
        high3 = high2
        high2 = high1
        high1 = (page,refs)
    elif refs > high2[1]:
        high3 = high2
        high2 = (page,refs)
    elif refs > high3[1]:
        high3 = (page,refs)

print("============= TOP 3 Pages ============= ")
print(f"Page: {high1[0]} Matches: {high1[1]}")
print(f"Page: {high2[0]} Matches: {high2[1]}")
print(f"Page: {high3[0]} Matches: {high3[1]}")
