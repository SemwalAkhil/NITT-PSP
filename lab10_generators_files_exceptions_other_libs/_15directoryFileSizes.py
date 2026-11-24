# 15. Write a program to traverse a directory and display file names and sizes in bytes.
# Input: ("."), ("..")
# Output:
#   Total files: 18
#   Total size: 30000 bytes

import os

folder = input("Enter folder path: ").strip() or "."

total_size = 0
file_count = 0

for root, dirs, files in os.walk(folder):
    for f in files:
        fp = os.path.join(root, f)
        try:
            sz = os.path.getsize(fp)
            total_size += sz
            file_count += 1
            print(f"{sz:>10} bytes | {fp}")
        except OSError:
            pass

print("-" * 50)
print("Total files:", file_count)
print("Total size:", total_size, "bytes")
