# 6. Write a program to add and subtract two polynomials represented by lists of coefficients.
# Input: ("2 0 3" "1 4 1"), ("1 2" "3 4")
# Output:
#   Run 1:
#   Add:  [3, 4, 4]
#   Sub:  [1, -4, 2]
#   Run 2:
#   Add:  [4, 6]
#   Sub:  [-2, -2]

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
    poly1 = [int(x) for x in input("Enter coefficients for polynomial 1: ").split()]
    poly2 = [int(x) for x in input("Enter coefficients for polynomial 2: ").split()]
    print("Add: ", addPoly(poly1, poly2))
    print("Sub: ", subPoly(poly1, poly2))
