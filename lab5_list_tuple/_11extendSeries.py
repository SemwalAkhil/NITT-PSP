series = (2, 5, 8, 11, 14)
n = int(input())

difference = series[1] - series[0]
result = list(series)

while len(result) < n:
    result.append(result[-1] + difference)

print(tuple(result))

