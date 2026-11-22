# 7. Write a program to validate date formats from a file using try-except ValueError and finally block.
# Input: None (data defined in the script)
# Output:
#   Valid date: 10-05-2026
#   Invalid date: 29-02-1909
#   Invalid date: 32-07-2006
#   Valid date: 29-02-2024
#   File closed successfully in finally block

from datetime import datetime

filename = "dates.txt"
with open(filename, "w") as f:
    f.write("10-05-2026\n29-02-1909\n32-07-2006\n29-02-2024\n")

f = None
try:
    f = open(filename, "r")
    for line in f:
        d_str = line.strip()
        if not d_str:
            continue
        try:
            valid_date = datetime.strptime(d_str, "%d-%m-%Y")
            print(f"Valid date: {d_str}")
        except ValueError:
            print(f"Invalid date: {d_str}")
except FileNotFoundError:
    print(f"File {filename} not found")
finally:
    if f is not None:
        f.close()
        print("File closed successfully in finally block")
