# 6. Write a program to move all zeros in a list to the end while maintaining relative order.
# Input: None (data defined in the script)
# Output: [1, 2, 3, 4, 50, 4, 6, 54, 6, 5, 8, 5, 6, 9, 5, 0, 0, 0, 0, 0]

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