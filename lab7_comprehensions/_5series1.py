# 5. Write a program to generate square number series 1 4 9 16 ... up to N terms using comprehension.
# Input: (4), (5)
# Output: 1 4 9 16, 1 4 9 16 25

print(" ".join([f"{i*i}" for i in range(1,int(input("Enter number of terms: "))+1)]))