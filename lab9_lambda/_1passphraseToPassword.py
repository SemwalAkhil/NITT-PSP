def passwordToPassphrase(phrases:list[str]=['carpet lemon thursday', 'Table Falcon Mirror Cloud', 'Pirate Eats Lemon Under Moon', 'Green Tiger Sings At Midnight', 'blue coffee runs before sunrise', 'obsessed reffried spectacle margarita']):
    password =  ["".join(map(lambda x: x[0] + str(ord(x[len(x)//2])) + x[-1],phrase.split())) for phrase in phrases]
    return password

if __name__ == "__main__":
    print(passwordToPassphrase())