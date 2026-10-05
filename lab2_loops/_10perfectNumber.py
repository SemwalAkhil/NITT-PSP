"""
Read n
s <- 0
For i <- 1 to floor(n/2) + 1 do
    If n % i = 0 do
        s <- s + i
If s = n do
    Print(Perfect)
Else do
    Print(Not Perfect)
"""
n:int = int(input("Enter a number: "))
s = 0
for i in range(1,n//2+1):
    s += i if n % i == 0 else 0
print("Perfect Number" if s == n else "Not Perfect Number")