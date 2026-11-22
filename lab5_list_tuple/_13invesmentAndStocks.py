# 13. Write a program to compute stock-wise, date-wise, and overall profit/loss from investment records.
# Input: None (data defined in the script)
# Output:
#   Stock-wise P/L:
#   Birla Cements : 0
#   TCS : 100
#   Date-wise P/L:
#   25-9-2026 : 0
#   26-9-2026 : 100
#   Overall P/L: 100

investments = [
    ('25-9-2026', 'Birla Cements', 500, 400),
    ('25-9-2026', 'TCS', 300, 400),
    ('26-9-2026', 'Birla Cements', 600, 700)
]

stocks = ()
dates = ()
overall = 0

for inv in investments:
    stock = inv[1]
    date = inv[0]
    pl = inv[3] - inv[2]
    overall += pl

    if stock not in stocks:
        stocks += (stock,)
    if date not in dates:
        dates += (date,)

print("Stock-wise P/L:")
for stock in stocks:
    total = 0
    for inv in investments:
        if inv[1] == stock:
            total += inv[3] - inv[2]
    print(stock, ":", total)

print("Date-wise P/L:")
for date in dates:
    total = 0
    for inv in investments:
        if inv[0] == date:
            total += inv[3] - inv[2]
    print(date, ":", total)

print("Overall P/L:", overall)