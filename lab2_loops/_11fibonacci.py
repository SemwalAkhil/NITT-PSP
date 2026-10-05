"""
Read n
left <- 0
right <- 1
Print(left)
For i <- 2 to i < n + 1 do
    Print(right)
    temp <- left
    left <- right
    right <- right + temp
"""
n:int = int(input("Number of terms: "))
left:int = 0
right:int = 1

print(left,end = " ")
for i in range(2,n+1):
    print(right,end = " ")
    left,right = right,right+left