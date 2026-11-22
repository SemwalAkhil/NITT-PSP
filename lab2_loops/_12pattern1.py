# 12. Write a program to print a right-angled decreasing number triangle pattern.
# Input: None (data defined in the script)
# Output:
#   1 2 3 4
#   1 2 3
#   1 2
#   1

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