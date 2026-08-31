'''
   1
  1 2
 1 2 3
1 2 3 4
'''
num: int = int(input("Enter number of rows: "))
for i in range(1, num+1):
    print(" "*(num-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print("")
