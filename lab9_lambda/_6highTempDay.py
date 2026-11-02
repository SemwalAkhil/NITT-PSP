temps = {"15-02-2023":33,"16-02-2023":56,"17-02-2023":77,"18-02-2023":23,"19-02-2023":46,"20-02-2023":90}
print("\n".join(map(lambda x: f"{x}: hot" if temps[x] > 50 else f"{x}: cold",temps.keys()))) 