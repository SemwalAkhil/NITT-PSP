# 18. Write a program to read datewise temperatures and classify them as hot (>50) or cold using map and lambda.
# Input: (6 15-02-2023 33 16-02-2023 56 17-02-2023 77 18-02-2023 23 19-02-2023 46 20-02-2023 90), (2 01-01-2023 25 02-01-2023 60)
# Output:
#   15-02-2023: cold
#   16-02-2023: hot
#   17-02-2023: hot
#   18-02-2023: cold
#   19-02-2023: cold
#   20-02-2023: hot

n = int(input("Enter number of days: "))
temps = {}
for i in range(n):
    d = input("Enter date (DD-MM-YYYY): ")
    t = int(input("Enter temperature: "))
    temps[d] = t

print("\n".join(map(lambda x: f"{x}: hot" if temps[x] > 50 else f"{x}: cold",temps.keys())))
