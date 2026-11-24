# 10. Write a program to generate a password from a passphrase using list comprehension.
# Input: (2 "correct horse battery staple" "ocean breeze mountain silent"), (1 "hello world")
# Output:
#   Run 1:
#   correct horse battery staple: cT114hE114bY116sE112
#   ocean breeze mountain silent: oN101bE101mN116sT101
#   Run 2:
#   hello world: hO108wD114

n = int(input("Enter number of passphrases: "))
passphrases = [input(f"Enter passphrase {i+1}: ") for i in range(n)]

pass_dict = {
    passphrase:"".join(word[0]+word[-1].upper()+str(ord(word[len(word)//2])) 
    for word in passphrase.split()) 
    for passphrase in passphrases
}
print(*(f"{key}: {value}\n" for key,value in pass_dict.items()),"\n")
