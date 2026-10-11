# Print a pattern in matrix
n = int(input("Enter number of rows: "))
matrix = [['*' for i in range(0,j)] for j in range(1,n)]
print("\n".join(["".join(row) for row in matrix]))