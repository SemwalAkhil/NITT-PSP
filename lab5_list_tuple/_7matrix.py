'''
7. Do all matrix operations (+,-,*,/, trace, transpose)

INPUT: A=[[1,2],[3,4]], B=[[5,6],[7,8]]
OUTPUT:
Addition: [[6,8],[10,12]]
Subtraction: [[-4,-4],[-4,-4]]
Multiplication: [[19,22],[43,50]]
Division: [[0.2,0.3333],[0.4286,0.5]]
Trace: 5
Transpose: [[1,3],[2,4]]

INPUT: A=[[2,0],[0,2]], B=[[1,1],[1,1]]
OUTPUT:
Addition: [[3,1],[1,3]]
Subtraction: [[1,-1],[-1,1]]
Multiplication: [[2,2],[2,2]]
Division: [[2,0],[0,2]]
Trace: 4
Transpose: [[2,0],[0,2]]
'''
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Addition:")
for i in range(2):
    print([A[i][j] + B[i][j] for j in range(2)])

print("Subtraction:")
for i in range(2):
    print([A[i][j] - B[i][j] for j in range(2)])

print("Multiplication:")
for i in range(2):
    row = []
    for j in range(2):
        total = 0
        for k in range(2):
            total += A[i][k] * B[k][j]
        row.append(total)
    print(row)

print("Division:")
for i in range(2):
    print([A[i][j] / B[i][j] for j in range(2)])

print("Trace:", A[0][0] + A[1][1])

print("Transpose:")
for j in range(2):
    print([A[i][j] for i in range(2)])