# 16. Write a program to map numbers to their squares using dictionary comprehension.
# Input: (4), (5)
# Output: {0: 0, 1: 1, 2: 4, 3: 9}, {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

n = int(input("Enter number of terms: "))
d = {num: num * num for num in range(n)}
print(d)
