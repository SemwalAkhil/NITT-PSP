n = int(input("Number of students in class: "))
donation = 0
for i in range(1,n+1):
    donation += i % 100
print("Total donation: ",donation)