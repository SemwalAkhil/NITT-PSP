'''
INPUT:  url(U)                                           https://example.com/index.html
OUTPUT: result(R)                                        https example.com /index.html
INPUT:  url(U)                                           ftp://sub.domain.org
OUTPUT: result(R)                                        ftp sub.domain.org /
'''
import re

url = input("Enter URL: ")
match = re.search(r"\b([A-Za-z][A-Za-z0-9\+\.\-]*)://([A-Za-z0-9-\.]+)(/[^\s]*)?\b", url)

if match:
    for item in match.groups():
        if item:
            print(item, end=" ")
        else:
            print("/", end=" ")
else:
    print("Invalid")