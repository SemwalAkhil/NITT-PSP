# 17. Write a program to map student names to their test scores using dictionary comprehension and zip.
# Input: None (data defined in the script)
# Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
print({name: score for name, score in zip(names, scores)})