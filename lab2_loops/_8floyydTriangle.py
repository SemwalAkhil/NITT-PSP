'''
1
2 3
4 5 6
7 8 9 10

Read n
c <- 1
For i <- 0 to n do
    For j <- 0 to i+1 do
        Print(c)
        c += 1
    Print(New line)
'''
n:int = int(input("Number of rows: "))
counter:int = 1
for i in range(0,n):
    for j in range(0,i+1):
        print(counter,end=" ")
        counter += 1
    print()