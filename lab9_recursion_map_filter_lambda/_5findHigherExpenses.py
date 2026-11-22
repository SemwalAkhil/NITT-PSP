# 5. Write a program to filter expenses exceeding a given amount using filter and lambda.
# Input: (1000), (500)
# Output: [('16-02-2023', 1200), ('18-02-2023', 2500)], [('16-02-2023', 1200), ('18-02-2023', 2500), ('19-02-2023', 800)]

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
