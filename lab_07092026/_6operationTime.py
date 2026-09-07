'''
PROBLEM STATEMENT: Given a string of operations find the (assumed) time it takes based on number of + - * / operations in it
INPUT: Algebraic Expression (A)
OUTPUT: Calculated time it'll take (T)
Read A
T <- 0
Add_Sub_Time <- 1
Mul_Div_Time <- 5
For i in A do
|   If i is '+' or '-'
|   |   T <- T + Add_Sub_Time
|   If i is '*' or '/'
|   |   T <- T + Mul_Div_Time
Write T
'''
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
