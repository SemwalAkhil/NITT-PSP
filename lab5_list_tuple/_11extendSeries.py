"""
11. Extend any series like ap, gp etc
INPUT: n(N)  8
OUTPUT: (2, 5, 8, 11, 14, 17, 20, 23)
INPUT: n(N)  3
OUTPUT: (2, 5, 8)
"""

series = (2, 5, 8, 11, 14)
n = int(input())

difference = series[1] - series[0]
result = list(series)

while len(result) < n:
    result.append(result[-1] + difference)

print(tuple(result))

