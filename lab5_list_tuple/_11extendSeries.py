# 11. Write a program to read an arithmetic progression series and extend it up to N elements.
# Input: ("2 5 8 11 14" 7), ("1 3 5" 5)
# Output: (2, 5, 8, 11, 14, 17, 20), (1, 3, 5, 7, 9)

series = tuple(int(x) for x in input("Enter series elements: ").split())
n = int(input("Enter total number of elements: "))

difference = series[1] - series[0]
result = list(series)

while len(result) < n:
    result.append(result[-1] + difference)

print(tuple(result))
