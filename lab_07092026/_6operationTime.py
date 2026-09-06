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
