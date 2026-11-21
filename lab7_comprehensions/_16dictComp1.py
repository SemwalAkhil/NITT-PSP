# store number and square in a dictionary
n = int(input("Enter number of terms: "))
d = {num: num * num for num in range(n)}
print(d)
