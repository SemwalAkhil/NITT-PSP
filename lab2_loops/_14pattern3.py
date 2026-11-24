# 14. Write a program to print a square matrix pattern of numbers.
# Input: (3), (4)
# Output:
#   Run 1:
#   1 2 3
#   1 2 3
#   1 2 3
#   Run 2:
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4
#   1 2 3 4

'''
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''
num: int = int(input("Enter number of rows: "))
for i in range(1, num+1):
    for j in range(1, num+1):
        print(j, end=" ")
    print("")
