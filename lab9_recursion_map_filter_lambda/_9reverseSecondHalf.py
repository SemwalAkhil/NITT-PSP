# 9. Write a program to reverse halves of words in a string using map and lambda.
# Input: ("flower garden"), ("python code")
# Output: rewflo nedgar, nohpyt edco

'''
F L O | W E R
R E W | F L O
'''
s = input("Enter string: ").split()
rev = " ".join(map(lambda x: x[len(x)//2:][::-1] + x[:len(x)//2],s))
print(rev)