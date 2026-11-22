# 15. Write a program to identify a substance given its boiling point within an error tolerance.
# Input: (100 5), (78.4 5)
# Output: Water, Ethanol

temp =  float(input("Enter a boiling point in degree celsus (C): "))
limit = float(input("Enter percentage limit (%): "))/100
found = False

if 100*(1-limit) <= temp <= 100*(1+limit):
    found = True
    print("Water")
if 78.4*(1-limit) <= temp <= 78.4*(1+limit):
    found = True
    print("Ethanol")
if 64.7*(1-limit) <= temp <= 64.7*(1+limit):
    found = True
    print("Methanol")
if not found:
    print("Substance not found")

