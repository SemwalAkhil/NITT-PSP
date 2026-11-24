# 1. Write a program to print a triangular star pattern using nested list comprehensions.
# Input: (3), (4)
# Output:
#   Run 1:
#   *
#   **
#   ***
#   Run 2:
#   *
#   **
#   ***
#   ****

n = int(input("Enter number of rows: "))
matrix = [['*' for i in range(0,j)] for j in range(1,n+1)]
print("\n".join(["".join(row) for row in matrix]))
