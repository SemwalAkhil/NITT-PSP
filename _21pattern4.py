'''
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''
num: int = int(input("Enter number of rows: "))
for i in range(1, num+1):
    for j in range(1, num+1):
        print(j, end=" ")
    print("")
