# 8. Write a program to calculate in-degree and out-degree of nodes in a directed graph using dictionaries.
# Input: (6 A "B C" B "A D E" C A D B E "B D" F "C A"), (3 1 "2 3" 2 3 3 1)
# Output:
#   Run 1:
#   A: OUT: 2 IN: 3
#   B: OUT: 3 IN: 3
#   C: OUT: 1 IN: 2
#   Run 2:
#   1: OUT: 2 IN: 1
#   2: OUT: 1 IN: 1
#   3: OUT: 1 IN: 2

num_nodes = int(input("Enter number of nodes: "))
graph = {}
for i in range(num_nodes):
    node = input("Enter node name: ")
    nbrs = input(f"Enter neighbours of {node}: ").split()
    graph[node] = nbrs

degrees = {node:[0,0] for node in graph.keys()}
similarity = {}

for node,others in graph.items():
    degrees[node][0] = len(others) 
    for other in others:
        if other in degrees:
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
