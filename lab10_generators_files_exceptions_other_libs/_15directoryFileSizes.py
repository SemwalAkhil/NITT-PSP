# 15. Write a program to traverse a directory and display file names and sizes in bytes.
# Input: ("sample_data/sample_folder")
# Output:
#          0 bytes | E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\sample_folder\empty.txt
#         18 bytes | E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\sample_folder\readme.txt
#         26 bytes | E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\sample_folder\docs\guide.txt
#         26 bytes | E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\sample_folder\docs\manual.txt
#         25 bytes | E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\sample_folder\docs\notes\ideas.txt
#         24 bytes | E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\sample_folder\docs\notes\todo.txt
#         30 bytes | E:\NITT-PSP-Lab\NITT-PSP\lab10_generators_files_exceptions_other_libs\sample_data\sample_folder\images\logo.txt
#   --------------------------------------------------
#   Total files: 7
#   Total size: 149 bytes

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
