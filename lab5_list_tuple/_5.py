'''
5. Find cumulative sum of a list
Ex: INPUT: [1,2,3,4]
    OUTPUT: [1,3,6,10]
    
INPUT: numbers(N)  [1, 2, 3, 4]
OUTPUT: [1, 3, 6, 10]
INPUT: numbers(N)  [2, 5, 1]
OUTPUT: [2, 7, 8]
'''
numbers = [1, 2, 3, 4]
result = []
total = 0

for num in numbers:
    total += num
    result.append(total)

print(result)