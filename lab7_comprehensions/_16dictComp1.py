# store number and square in a dictionary
print(*(f"{key}: {key * key}\n" for key in [num for num in range(int(input("Enter number of terms: ")))]))