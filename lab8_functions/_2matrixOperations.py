# 2. Write functions to add, subtract, multiply, and transpose matrices.
# Input: (2 2 1 2 3 4 2 2 5 6 7 8), (1 2 1 2 2 1 3 4)
# Output:
#   Add:  [[6, 8], [10, 12]]
#   Sub:  [[-4, -4], [-4, -4]]
#   Mul:  [[19, 22], [43, 50]]
#   Trans:  [[1, 3], [2, 4]]

def add(mat1:list[list[int]],mat2:list[list[int]]):
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        ans = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[0])):
                row.append(mat1[i][j] + mat2[i][j])
            ans.append(row)
        return ans
    else:
        return []

def sub(mat1:list[list[int]],mat2:list[list[int]]):
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        ans = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat1[0])):
                row.append(mat1[i][j] - mat2[i][j])
            ans.append(row)
        return ans
    else:
        return []

def mul(mat1:list[list[int]],mat2:list[list[int]]):
    if len(mat1[0]) == len(mat2):
        ans = []
        for i in range(len(mat1)):
            row = []
            for j in range(len(mat2[0])):
                total = 0
                for k in range(len(mat2)):
                    total += mat1[i][k] * mat2[k][j]
                row.append(total)
            ans.append(row)
        return ans
    else:
        return []

def trans(mat:list[list[int]]):
    if len(mat) == 0:
        return []
    ans = []
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        ans.append(row)
    return ans

if __name__ == "__main__":
    r1 = int(input("Enter matrix 1 rows: "))
    c1 = int(input("Enter matrix 1 cols: "))
    m1 = []
    for i in range(r1):
        m1.append([int(x) for x in input(f"Enter row {i+1} for matrix 1: ").split()])

    r2 = int(input("Enter matrix 2 rows: "))
    c2 = int(input("Enter matrix 2 cols: "))
    m2 = []
    for i in range(r2):
        m2.append([int(x) for x in input(f"Enter row {i+1} for matrix 2: ").split()])

    print("Add: ", add(m1, m2))
    print("Sub: ", sub(m1, m2))
    print("Mul: ", mul(m1, m2))
    print("Trans: ", trans(m1))
