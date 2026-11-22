# 20. Write a program to perform a case-insensitive check whether a given phrase is a palindrome.
# Input: (racecar), (hello)
# Output: Pallindrome, Not Pallindrome

string = input("Enter a phrase: ").lower()
if string == string[::-1]:
    print("Pallindrome")
else:
    print("Not Pallindrome")
