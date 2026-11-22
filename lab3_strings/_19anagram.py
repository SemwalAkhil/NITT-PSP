# 19. Write a program to check if two strings are anagrams of each other.
# Input: (listen silent), (hello world)
# Output: Anagram, Not Anagram

string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")
if len(string1) == len(string2):
    if sorted(string1) == sorted(string2):
        print("Anagram")
    else:
        print("Not Anagram")
else:
    print("Not Anagram")
