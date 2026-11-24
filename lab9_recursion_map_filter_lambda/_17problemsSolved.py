# 17. Write a program to sum problems solved per topic and find the maximum topic using map, lambda, and reduce.
# Input: (4 list "5 4 6" tuple "3 4 7" regex "1 2 6" strings "3 2 6"), (2 math "5 5" logic "10 2")
# Output:
#   Run 1:
#   list: 15
#   tuple: 14
#   regex: 9
#   strings: 11
#   Max:  list
#   Run 2:
#   math: 10
#   logic: 12
#   Max:  logic

import functools as f

n = int(input("Enter number of topics: "))
solved = {}
for i in range(n):
    topic = input("Enter topic name: ")
    counts = [int(x) for x in input(f"Enter solved counts for {topic}: ").split()]
    solved[topic] = counts

total_solved = dict(map(lambda x: (x,sum(solved[x])),solved))
max_q = f.reduce(lambda x,y: x if total_solved[x] > total_solved[y] else y,total_solved.keys())
print("\n".join(map(lambda x: f"{x}: {total_solved[x]}", total_solved)))
print("Max: ",max_q)
