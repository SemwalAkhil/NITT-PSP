'''
F L O | W E R
R E W | F L O
'''
s = input("Enter string: ").split()
rev = " ".join(map(lambda x: x[len(x)//2:][::-1] + x[:len(x)//2],s))
print(rev)