'''
1 2 3 4
1 2 3
1 2
1
'''

for i in range(0,4):
    for j in range(0,4-i):
        print(j+1,end=" ")
    print()