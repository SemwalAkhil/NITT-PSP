"""
Read n
d <- 0
For i <- 1 to n+1 do
    d <- d + i
Print(d)
"""
n:int = int(input("Number of students in class: "))
donation:int = 0
for i in range(1,n+1):
    donation += i 
print("Total donation: ",donation)