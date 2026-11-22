# 5. Write a program to filter expenses exceeding a given amount using filter and lambda.
# Input: (5 15-02-2023 500 16-02-2023 1200 17-02-2023 300 18-02-2023 2500 19-02-2023 800 1000), (2 01-01-2023 400 02-01-2023 700 500)
# Output: [('16-02-2023', 1200), ('18-02-2023', 2500)], [('02-01-2023', 700)]

n = int(input("Enter number of expenses: "))
expenses = []
for i in range(n):
    d = input("Enter date (DD-MM-YYYY): ")
    amt = int(input("Enter amount: "))
    expenses.append((d, amt))

limit = float(input("Enter expense limit: "))
higher = list(filter(lambda x: x[1] > limit, expenses))
print(higher)
