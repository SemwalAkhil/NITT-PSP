# 2. Write a program to allocate contiguous blocks in a 0-1 list and print the resulting list.
# Input: (2), (3)
# Output:
#   Run 1:
#   [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
#   [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
#   Run 2:
#   [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
#   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

blocks = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

print(blocks)
inserts = int(input())

if blocks.count(1) < inserts:
    print("Not enough empty spaces")
else:
    for i in range(inserts):
        blocks[blocks.index(1)] = 0
    print(blocks)