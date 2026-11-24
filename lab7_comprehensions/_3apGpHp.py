# 3. Write a program to generate AP, GP, and HP series using list comprehensions.
# Input: (1 2 4), (2 3 3)
# Output:
#   Run 1:
#   AP:  [1, 3, 5, 7]
#   GP:  [1, 2, 4, 8]
#   HP:  ['1/1', '1/3', '1/5', '1/7']
#   Run 2:
#   AP:  [2, 5, 8]
#   GP:  [2, 6, 18]
#   HP:  ['1/2', '1/5', '1/8']

a = int(input("Enter first term: "))
d = int(input("Enter first common difference/ratio: "))
num = int(input("Enter number of terms: "))
print("AP: ",[a + (n-1)*d for n in range(1,num+1)])
print("GP: ",[a * d ** (n-1) for n in range(1,num+1)])
print("HP: ",[f"1/{a + (n-1)*d}" for n in range(1,num+1)])
