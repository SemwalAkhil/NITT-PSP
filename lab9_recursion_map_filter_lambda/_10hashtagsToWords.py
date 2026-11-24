# 10. Write a program to convert camelCase hashtags into separated words using regular expressions.
# Input: ("#HelloWorld #PythonLab"), ("#QuickBrown #FoxJumps")
# Output:
#   Run 1:
#   Hello World
#   Python Lab
#   Run 2:
#   Quick Brown
#   Fox Jumps

import re
hashtags = input("Enter hashtag: ").split()
print("\n".join(map(lambda x: " ".join(re.findall("([A-Z][a-z]*)",x)),hashtags)))