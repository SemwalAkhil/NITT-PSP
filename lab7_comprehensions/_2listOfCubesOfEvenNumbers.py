# Print list of cubes of even numbers
print([natural ** 3 for natural in range(1,int(input("Enter number of natural numbers: "))+1) if natural % 2 == 0])
