marks = {
    1 : [60,80,30,70],
    2 : [90,60,50,40],
    3 : [10,50,30,40],
}
print("\n".join(map(lambda x: f"{x}:{sum(marks[x])/len(marks[x])}%",marks.keys())))
