# 1. Write a function to generate passwords from passphrases using map and lambda.
# Input: None (data defined in the script)
# Output: ['c112tl109nt115y', 'T98eF99nM114rC111d', 'P97eE116sL109nU100rM111n', 'G101nT103rS110sA116tM105t', 'b117ec102er110sb111es114e', 'o115dr114ds116em97a']

def passphraseToPassword(phrases:list[str]=['carpet lemon thursday', 'Table Falcon Mirror Cloud', 'Pirate Eats Lemon Under Moon', 'Green Tiger Sings At Midnight', 'blue coffee runs before sunrise', 'obsessed reffried spectacle margarita']):
    password =  ["".join(map(lambda x: x[0] + str(ord(x[len(x)//2])) + x[-1],phrase.split())) for phrase in phrases]
    return password

if __name__ == "__main__":
    print(passphraseToPassword())
