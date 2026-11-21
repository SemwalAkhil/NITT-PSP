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
    m1 = [[1, 2], [3, 4]]
    m2 = [[5, 6], [7, 8]]
    print("Add: ", add(m1, m2))
    print("Sub: ", sub(m1, m2))
    print("Mul: ", mul(m1, m2))
    print("Trans: ", trans(m1))
