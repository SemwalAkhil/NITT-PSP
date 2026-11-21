n:int = int(input("Number of terms: "))
left:int = 0
right:int = 1

print(left,end = " ")
for i in range(2,n+1):
    print(right,end = " ")
    left,right = right,right+left