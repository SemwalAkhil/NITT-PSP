# 15. Write a program to print a palindromic number pyramid pattern for N rows.
# Input: (3), (4)
# Output:
#       1
#     1 2 1
#   1 2 3 2 1

'''
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
'''
num: int = int(input("Enter number of rows: "))
for i in range(1, num+1):
    print(" "*(num-i)*2, end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print("")
