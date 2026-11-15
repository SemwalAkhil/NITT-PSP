# define functions to add, sub, multiply, transpose a matrix
def add(mat1:list[list[int]],mat2:list[list[int]]):
    if (0 != len(mat1) == len(mat2) != 0 or len(mat1[0]) == len(mat2[0])):
        ans = []
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                ans[len(mat1)][len(mat1[0])] = mat1[i][j] + mat2[i][j]  
        return ans
    else:
        return []
def sub(mat1:list[list[int]],mat2:list[list[int]]):
    if (0 != len(mat1) == len(mat2) != 0 or len(mat1[0]) == len(mat2[0])):
        ans = []
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                ans[len(mat1)][len(mat1[0])] = mat1[i][j] - mat2[i][j]  
        return ans
    else:
        return []

def mul(mat1:list[list[int]],mat2:list[list[int]]):
    if ((0 != len(mat1) == len(mat2) != 0) or (0 != len(mat1[0]) == len(mat2[0]) != 0)):
        ans = []
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                ans[len(mat1)][len(mat1[0])] = mat1[i][j] + mat2[i][j]  
        return ans
    else:
        return []
def sub(mat1:list[list[int]],mat2:list[list[int]]):
    if (0 != len(mat1) == len(mat2) != 0 or len(mat1[0]) == len(mat2[0])):
        ans = []
        for i in range(len(mat1)):
            for j in range(len(mat1[0])):
                ans[len(mat1)][len(mat1[0])] = mat1[i][j] - mat2[i][j]  
        return ans
    else:
        return []
