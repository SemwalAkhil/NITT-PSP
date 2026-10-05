# 0 -> absent 1 -> present; Number of absent/present
blocks = [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
print("Current blocks")
print(blocks)
inserts = int(input("Enter number of insertions : "))
if blocks.count(0) < inserts:
    print("Not enough empty spaces")
else:
    for i in range(inserts):
        blocks[blocks.index(0)] = 1

    print(blocks)
