# 17. Write a program to read student names and test scores and map them using dictionary comprehension and zip.
# Input: ("Alice Bob Charlie" "85 92 78"), ("John Doe" "90 80")
# Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}, {'John': 90, 'Doe': 80}

names = input("Enter student names: ").split()
scores = [int(x) for x in input("Enter test scores: ").split()]
print({name: score for name, score in zip(names, scores)})
