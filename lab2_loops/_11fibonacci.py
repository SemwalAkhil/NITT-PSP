# 11. Write a program to print the first N terms of the Fibonacci sequence.
# Input: (5), (7)
# Output: 0 1 1 2 3, 0 1 1 2 3 5 8

n:int = int(input("Number of terms: "))
left:int = 0
right:int = 1

print(left,end = " ")
for i in range(2,n+1):
    print(right,end = " ")
    left,right = right,right+left