# 18. Write a program to classify datewise temperatures as hot (>50) or cold using map and lambda.
# Input: None (data defined in the script)
# Output:
#   15-02-2023: cold
#   16-02-2023: hot
#   17-02-2023: hot
#   18-02-2023: cold
#   19-02-2023: cold
#   20-02-2023: hot

temps = {"15-02-2023":33,"16-02-2023":56,"17-02-2023":77,"18-02-2023":23,"19-02-2023":46,"20-02-2023":90}
print("\n".join(map(lambda x: f"{x}: hot" if temps[x] > 50 else f"{x}: cold",temps.keys()))) 