blocks = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]

print(blocks)
inserts = int(input())

if blocks.count(1) < inserts:
    print("Not enough empty spaces")
else:
    for i in range(inserts):
        blocks[blocks.index(1)] = 0
    print(blocks)