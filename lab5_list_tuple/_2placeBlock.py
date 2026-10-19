'''
2. List of free space given containing 0,1 etc. Ex: [0, 1, 1, 1,,0,0,1,1] .0 means full, 1 means empty. From user, ask how many blocks to store. Store if you can else show full.

INPUT:  inserts(I)  2
OUTPUT: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

INPUT:  inserts(I)  6
OUTPUT: Not enough empty spaces
'''
blocks = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

print(blocks)
inserts = int(input())

if blocks.count(1) < inserts:
    print("Not enough empty spaces")
else:
    for i in range(inserts):
        blocks[blocks.index(1)] = 0
    print(blocks)