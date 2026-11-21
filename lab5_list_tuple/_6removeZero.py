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