# 11. Write a program to classify coordinate tuples into quadrants and axes using dictionary comprehension.
# Input: None (data defined in the script)
# Output:
#   I: [(1, 2)]
#   II: [(-2, 3)]
#   III: [(-5, -5)]
#   IV: [(4, -1)]
#   O: [(0, 0), (0, 0)]

coords = [(1,2),(-2,3),(0,1),(-1,0),(0,0),(4,-1),(-5,-5),(0,0),(0,-5),(6,0)]
quadrants = {
    "I": [coord for coord in coords if coord[0] > 0 and coord[1] > 0],
    "II": [coord for coord in coords if coord[0] < 0 and coord[1] > 0],
    "III": [coord for coord in coords if coord[0] < 0 and coord[1] < 0],
    "IV": [coord for coord in coords if coord[0] > 0 and coord[1] < 0],
    "O": [coord for coord in coords if coord[0] == 0 and coord[1] == 0],
    "X": [coord for coord in coords if coord[0] == 0 and coord[1] != 0],
    "Y": [coord for coord in coords if coord[0] != 0 and coord[1] == 0]
}

print(*(f"{key}: {value}\n" for key,value in quadrants.items()),"\n")
"""
    The unpacking operator (*) takes an iterable (like a list, tuple, or generator) and unpacks its items so they are passed as individual arguments rather than as a single collection.    
"""