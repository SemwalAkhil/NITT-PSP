# 4. Write a program to filter all three-digit Armstrong numbers between 100 and 1000 using filter and lambda.
# Input: None (data defined in the script)
# Output: [153, 370, 371, 407]

armstrongs = list(filter(lambda n: sum(int(d)**3 for d in str(n)) == n, range(100, 1000)))
print(armstrongs)
