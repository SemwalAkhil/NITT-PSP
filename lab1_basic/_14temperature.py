# 14. Write a program to convert temperature from Celsius to Fahrenheit.
# Input: (100), (0)
# Output: Fahrenheit: 212.00, Fahrenheit: 32.00

c:float = float(input("Enter temperature celsius: "))
print("Fahrenheit: {:.2f}".format(((9/5)*c) + 32) )