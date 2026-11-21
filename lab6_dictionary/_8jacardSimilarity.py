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
        if node1 != node2 and not similarity.get(f"{node2}-{node1}",False):
            nbr1 = set(graph[node1])
            nbr2 = set(graph[node2])
            inter = list(nbr1.intersection(nbr2))
            union = list(nbr1.union(nbr2))
            jacard = len(inter)/len(union) if len(union) > 0 else 0.0
            similarity[f"{node1}-{node2}"] = (inter,union,jacard)

print(similarity)
