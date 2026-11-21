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