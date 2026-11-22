# 17. Write a program to aggregate problem counts and find the category with max solved using reduce.
# Input: None (data defined in the script)
# Output:
#   list: 15
#   tuple: 14
#   regex: 9
#   strings: 11
#   Max:  list

import functools as f
solved = {
    "list":[5,4,6],
    "tuple":[3,4,7],
    "regex":[1,2,6],
    "strings":[3,2,6],
}
total_solved = dict(map(lambda x: (x,sum(solved[x])),solved))
max_q = f.reduce(lambda x,y: x if total_solved[x] > total_solved[y] else y,total_solved.keys())
print("\n".join(map(lambda x: f"{x}: {total_solved[x]}", total_solved)))
print("Max: ",max_q)
