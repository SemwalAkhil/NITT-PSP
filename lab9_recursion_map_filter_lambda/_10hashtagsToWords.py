# 10. Write a program to split hashtags into separated words using map, lambda, and regex.
# Input: ("#HelloWorld #PythonLab"), ("#QuickBrown #FoxJumps")
# Output:
#   Hello World
#   Python Lab

import re
hashtags = input("Enter hashtag: ").split()
print("\n".join(map(lambda x: " ".join(re.findall("([A-Z][a-z]*)",x)),hashtags)))