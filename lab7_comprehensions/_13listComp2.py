# Enter an array from user and print all the palindrome numbers?
n1 = int(input("Number of elements in list: "))
l1 = []
for i in range(n1):
    l1.append(input(f"{i+1} element: "))

print([i for i in l1 if i == i[::-1]])

