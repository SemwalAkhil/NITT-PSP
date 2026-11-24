# 12. Write a program to classify temperatures as hot (>50) or cold (<=50) using map and lambda.
# Input: ("33 56 77 23 46 90"), ("25 60")
# Output:
#   Run 1:
#   33: cold
#   56: hot
#   77: hot
#   23: cold
#   46: cold
#   90: hot
#   Run 2:
#   25: cold
#   60: hot

temps = [int(x) for x in input("Enter temperatures: ").split()]
print("\n".join(map(lambda x: f"{x}: hot" if x > 50 else f"{x}: cold",temps)))
