# 10. Write a program to generate passwords from passphrases using dictionary comprehension.
# Input: None (data defined in the script)
# Output:
#   correct horse battery staple: cT114hE114bY116sE112
#   ocean breeze mountain silent: oN101bE101mN116sT101
#   guitar planet velvet shadow: gR116pT110vT118sW100
#   pencil lantern thunder cookie: pL99lN116tR110

passphrases = [
    "correct horse battery staple",
    "ocean breeze mountain silent",
    "guitar planet velvet shadow",
    "pencil lantern thunder cookie",
    "falcon river copper blossom"
]
pass_dict = {
    passphrase:"".join(word[0]+word[-1].upper()+str(ord(word[len(word)//2])) 
    for word in passphrase.split()) 
    for passphrase in passphrases
}
print(*(f"{key}: {value}\n" for key,value in pass_dict.items()),"\n")