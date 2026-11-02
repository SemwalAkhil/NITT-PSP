"""
14. For a trip expenses. Show the share per person. Average amount paid by each person. How much one owes to another

INPUT: payments(P) (("A", 300), ("B", 100))
OUTPUT:
Total expense: 400
Share per person: 200.0
Average amount paid: 200.0
B owes A : 100.0

INPUT: payments(P) (("A", 100), ("B", 100))
OUTPUT:
Total expense: 200
Share per person: 100.0
Average amount paid: 100.0
"""
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