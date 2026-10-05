# pallindrome (Case insensitive check)

string = input("Enter a phrase: ").lower()
if string == string[::-1]:
    print("Pallindrome")
else:
    print("Not Pallindrome")
