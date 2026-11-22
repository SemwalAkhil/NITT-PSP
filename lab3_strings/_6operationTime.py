# 6. Write a program to compute operation time based on operators present in an expression string.
# Input: ("1+2*3-4/5"), ("10+20-30")
# Output: 12 units, 2 units

ADD_SUB = 1
MUL_DIV = 5
oprs = input("Enter string of operations (Integers and + - * /): ")
time = 0
for i in oprs:
    if i in "+-":
        time += ADD_SUB
    if i in "*/":
        time += MUL_DIV
print(f"{time} units")
