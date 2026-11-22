# 12. Write a program to classify temperatures as hot (>50) or cold using map and lambda.
# Input: None (data defined in the script)
# Output:
#   33: cold
#   56: hot
#   77: hot
#   23: cold
#   46: cold
#   90: hot

temps = [33,56,77,23,46,90]
print("\n".join(map(lambda x: f"{x}: hot" if x > 50 else f"{x}: cold",temps))) 