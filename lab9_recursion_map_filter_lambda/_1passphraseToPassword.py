# 1. Write a function to generate passwords from passphrases using map and lambda.
# Input: (2 "carpet lemon thursday" "Table Falcon Mirror Cloud"), (1 "hello world")
# Output: ['c112tl109nt115y', 'T98eF99nM114rC111d'], ['h101ow114d']

def passphraseToPassword(phrases:list[str]=None):
    if phrases is None:
        phrases = []
    password =  ["".join(map(lambda x: x[0] + str(ord(x[len(x)//2])) + x[-1],phrase.split())) for phrase in phrases]
    return password

if __name__ == "__main__":
    n = int(input("Enter number of passphrases: "))
    p_list = [input(f"Enter passphrase {i+1}: ") for i in range(n)]
    print(passphraseToPassword(p_list))
