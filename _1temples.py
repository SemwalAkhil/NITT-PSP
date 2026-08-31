flowers = int(input("Number of flowers on each temple: "))
temples = int(input("Number of temples: "))
if (flowers % 2 ** temples != 0):
    print("Invalid number of flowers")
else:
    initial = 0
    for i in range(0,temples):
        initial = initial + flowers
        initial = initial/2
    print("Initial number of flowers: ",initial)