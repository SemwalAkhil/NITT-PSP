# 2. Write a program to fill empty spaces (1s) in a block list with occupied markers (0s).
# Input: (2), (3)
# Output:
#   [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
#   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

blocks = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

print(blocks)
inserts = int(input())

if blocks.count(1) < inserts:
    print("Not enough empty spaces")
else:
    for i in range(inserts):
        blocks[blocks.index(1)] = 0
    print(blocks)