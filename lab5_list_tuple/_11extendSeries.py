# 11. Write a program to extend an arithmetic progression tuple up to N elements.
# Input: (7), (8)
# Output: (2, 5, 8, 11, 14, 17, 20), (2, 5, 8, 11, 14, 17, 20, 23)

series = (2, 5, 8, 11, 14)
n = int(input())

difference = series[1] - series[0]
result = list(series)

while len(result) < n:
    result.append(result[-1] + difference)

print(tuple(result))

