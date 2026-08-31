'''
4 3 2 1
  3 2 1
    2 1
      1
'''
for i in range(0,4):
    print(" "*i*2,end="")
    for j in range(4-i,0,-1):
        print(j,end=" ")
    print()