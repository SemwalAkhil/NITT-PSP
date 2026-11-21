expenses = [
    ("15-02-2023", 500),
    ("16-02-2023", 1200),
    ("17-02-2023", 300),
    ("18-02-2023", 2500),
    ("19-02-2023", 800)
]

limit = float(input("Enter expense limit: "))
higher = list(filter(lambda x: x[1] > limit, expenses))
print(higher)
