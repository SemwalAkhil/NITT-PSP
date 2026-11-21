payments = (("A", 500), ("B", 300), ("C", 100))
total = 0

for person in payments:
    total += person[1]

share = total / len(payments)
print("Total expense:", total)
print("Share per person:", share)
print("Average amount paid:", share)

balances = ()

for person in payments:
    balances += ((person[0], person[1] - share),)

for person in balances:
    if person[1] < 0:
        for other in balances:
            if other[1] > 0:
                amount = min(-person[1], other[1])
                print(person[0], "owes", other[0], ":", round(amount, 2))
                balances = tuple(
                    (p[0], p[1] + amount if p[0] == person[0]
                     else p[1] - amount if p[0] == other[0] else p[1])
                    for p in balances
                )
                break