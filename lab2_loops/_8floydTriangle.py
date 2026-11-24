# 8. Write a program to print Floyd's triangle for N rows using nested loops.
# Input: (4), (3)
# Output:
#   1
#   2 3
#   4 5 6
#   7 8 9 10

'''
1
2 3
4 5 6
7 8 9 10
'''
n:int = int(input("Number of rows: "))
counter:int = 1
for i in range(0,n):
    for j in range(0,i+1):
        print(counter,end=" ")
        counter += 1
    print()