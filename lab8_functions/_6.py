# 6. Write functions to add and subtract two polynomials represented as coefficient lists.
# Input: poly1=[2, 0, 3], poly2=[1, 4, 1]
# Output:
#   Add:  [3, 4, 4]
#   Sub:  [1, -4, 2]

def addPoly(p1: list[int], p2: list[int]):
    n = max(len(p1), len(p2))
    res = [0] * n
    for i in range(len(p1)):
        res[i] += p1[i]
    for i in range(len(p2)):
        res[i] += p2[i]
    return res

def subPoly(p1: list[int], p2: list[int]):
    n = max(len(p1), len(p2))
    res = [0] * n
    for i in range(len(p1)):
        res[i] += p1[i]
    for i in range(len(p2)):
        res[i] -= p2[i]
    return res

if __name__ == "__main__":
    poly1 = [2, 0, 3]  # 2 + 3x^2
    poly2 = [1, 4, 1]  # 1 + 4x + x^2
    print("Add: ", addPoly(poly1, poly2))
    print("Sub: ", subPoly(poly1, poly2))
