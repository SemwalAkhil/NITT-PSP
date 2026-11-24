# 14. Write a program to split trip expenses among friends and calculate who owes whom.
# Input: (3 A 500 B 300 C 100), (2 Alice 200 Bob 100)
# Output:
#   Run 1:
#   Total expense: 900
#   Share per person: 300.0
#   Average amount paid: 300.0
#   C owes A : 200.0
#   Run 2:
#   Total expense: 300.0
#   Share per person: 150.0
#   Average amount paid: 150.0
#   Bob owes Alice : 50.0

n = int(input("Enter number of people: "))
temp_payments = []
for i in range(n):
    name = input("Enter name: ")
    amt = float(input("Enter amount paid: "))
    temp_payments.append((name, amt))
payments = tuple(temp_payments)

total = 0

for person in payments:
    total += person[1]

share = total / len(payments)
print("Total expense:", total)
print("Share per person:", share)
print("Average amount paid:", share)

balances = []

for person in payments:
    balances.append([person[0], person[1] - share])

for i in range(len(balances)):
    if balances[i][1] < 0:
        for j in range(len(balances)):
            if balances[j][1] > 0 and balances[i][1] < 0:
                amount = min(-balances[i][1], balances[j][1])
                print(balances[i][0], "owes", balances[j][0], ":", round(amount, 2))
                balances[i][1] += amount
                balances[j][1] -= amount
