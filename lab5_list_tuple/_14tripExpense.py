payments = (("A", 500), ("B", 300), ("C", 100))
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
