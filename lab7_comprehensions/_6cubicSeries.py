# 6. Write a program to generate terms of a cubic difference series using list comprehension.
# Input: (-10 5), (0 4)
# Output: [-10, -8, 6, 40, 102], [0, 2, 16, 50]

''' 
-10 -8  6  40  102
   2  14 34  62
    12  20 28
      8   8
=> Ax^3 + Bx^2 + Cx + D
solve by putting x in equation and equating to terms in series
'''
start =  int(input("Enter first term: "))
n_terms = int(input("Enter number of terms: ")) # Enter 5

a = [round((4/3)*(i**3) + 2*(i**2) - (4/3)*i + start) for i in range(n_terms)]
print(a)
