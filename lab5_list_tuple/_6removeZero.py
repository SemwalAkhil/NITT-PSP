'''
6. List with 0's in between. Pust all 0's to the end and remaining order should be same
Ex; INPUT:  [1,2,3,4,50,4,6,0,54,6,0,5,8,0,5,6,0,9,5,0]
    OUTPUT: [1, 2, 3, 4, 50, 4, 6, 54, 6, 5, 8, 5, 6, 9, 5, 0, 0, 0, 0, 0]

INPUT: numbers(N)  [1, 0, 2]
OUTPUT: [1, 2, 0]
INPUT: numbers(N)  [0, 0, 3]
OUTPUT: [3, 0, 0]
'''
numbers = [1, 2, 3, 4, 50, 4, 6, 0, 54, 6, 0, 5, 8, 0, 5, 6, 0, 9, 5, 0]
result = []
count = 0

for num in numbers:
    if num != 0:
        result.append(num)
    else:
        count += 1

for i in range(count):
    result.append(0)

print(result)