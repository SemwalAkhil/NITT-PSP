# 11. Write a program to classify 2D coordinates into quadrants using dictionary comprehension.
# Input: (3 "1 2" "-2 3" "0 0"), (2 "4 -1" "-5 -5")
# Output:
#   Run 1:
#   I: [(1, 2)]
#   II: [(-2, 3)]
#   O: [(0, 0)]
#   Run 2:
#   III: [(-5, -5)]
#   IV: [(4, -1)]

n = int(input("Enter number of coordinates: "))
coords = []
for i in range(n):
    point = input("Enter x and y: ").split()
    coords.append((int(point[0]), int(point[1])))

quadrants = {
    "I": [coord for coord in coords if coord[0] > 0 and coord[1] > 0],
    "II": [coord for coord in coords if coord[0] < 0 and coord[1] > 0],
    "III": [coord for coord in coords if coord[0] < 0 and coord[1] < 0],
    "IV": [coord for coord in coords if coord[0] > 0 and coord[1] < 0],
    "O": [coord for coord in coords if coord[0] == 0 and coord[1] == 0],
    "X": [coord for coord in coords if coord[0] == 0 and coord[1] != 0],
    "Y": [coord for coord in coords if coord[0] != 0 and coord[1] == 0]
}

print(*(f"{key}: {value}\n" for key,value in quadrants.items() if len(value) > 0),"\n")
"""
    The unpacking operator (*) takes an iterable (like a list, tuple, or generator) and unpacks its items so they are passed as individual arguments rather than as a single collection.    
"""
