# 7. Write a program to calculate the total donation where student i donates i amount.
# Input: (5), (10)
# Output: Total donation:  15, Total donation:  55

n:int = int(input("Number of students in class: "))
donation:int = 0
for i in range(1,n+1):
    donation += i 
print("Total donation: ",donation)