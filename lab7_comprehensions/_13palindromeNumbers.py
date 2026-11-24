# 13. Write a program to filter palindrome strings from user input using list comprehension.
# Input: (3 racecar hello madam), (2 noon world)
# Output: ['racecar', 'madam'], ['noon']

n1 = int(input("Number of elements in list: "))
l1 = []
for i in range(n1):
    l1.append(input(f"{i+1} element: "))

print([i for i in l1 if i == i[::-1]])

