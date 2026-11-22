# 5. Write a program to compute the prefix running sum of a list of numbers.
# Input: None (data defined in the script)
# Output: [1, 3, 6, 10]

numbers = [1, 2, 3, 4]
result = []
total = 0

for num in numbers:
    total += num
    result.append(total)

print(result)