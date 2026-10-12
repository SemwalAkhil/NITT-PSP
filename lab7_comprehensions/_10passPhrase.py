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