graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A"],
    "D": ["B"],
    "E": ["B","D"],
    "F": ["C","A"]
}
degrees = {node:[0,0] for node in graph.keys()}
similarity = {}

for node,others in graph.items():
    degrees[node][0] = len(others) 
    for other in others:
        degrees[other][1] += 1

for node,degree in degrees.items():
    print(f"{node}: OUT: {degree[0]} IN: {degree[1]}")

for node1 in graph:
    for node2 in graph:
        if not similarity.get(f"{node2}-{node1}",False):
            inter = []
            union = []
            small = node1 if degrees[node2][0] > degrees[node1][0] else node2
            big = node1 if small == node2 else node2
            for out in small:
                if out in big:
                    inter.append(out)
            print(inter)
            for out in small:
                if out not in big:
                    union.append(out)
            print(union)
            jacard = len(inter)/len(union)
            similarity[f"{node2}-{node1}"] = (inter,union,jacard)

print(similarity)
