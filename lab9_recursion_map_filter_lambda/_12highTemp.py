# 12. Write a program to read temperatures and classify them as hot (>50) or cold using map and lambda.
# Input: ("33 56 77 23 46 90"), ("25 60")
# Output:
#   33: cold
#   56: hot
#   77: hot
#   23: cold
#   46: cold
#   90: hot

temps = [int(x) for x in input("Enter temperatures: ").split()]
print("\n".join(map(lambda x: f"{x}: hot" if x > 50 else f"{x}: cold",temps)))
