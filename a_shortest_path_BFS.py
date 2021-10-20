import sys
sys.path.append('C:\\Users\\acer\\basic_algorithms_python\\graph')

from graph import Graph


"""
Here, we implement an algorithm to find a shortest path between two vertices of a connected graph 
using Breath-First Search strategy.
"""


def find_a_shortest_path(graph, v1, v2):
    layers = graph.BFS_layers(v2)
    path = [v1]
    if v1 == v2:
        return path
    elif v1 in layers[1]:
        path.append(v2)
        return path
    n = len(layers)  # so n must be at least 3
    for i in range(2, n):
        if v1 in layers[i]:
            n = i
            break
    while i > 1:
        for vertex in graph.adj_list[path[-1]]:
            if vertex in layers[i - 1]:
                path.append(vertex)
                i -= 1
                break
    path.append(v2)
    return path, n  # We return n to test our algorithm


g = Graph()
edges = [["A", "B"], ["A", "C"], ["D", "C"], ["B", "E"], ["F", "D"], ["F", "E"], ["G", "F"], ["H", "G"],
         ["H", "D"], ["G", "I"], ["J", "G"], ["K", "J"],  ["K", "L"], ["I", "L"],
         ["L", "M"], ["L", "N"], ["L", "O"], ["O", "R"], ["N", "R"]]
g.from_edge_list(edges)
print(g)
v1 = "A"
v2 = "R"
print("The list of layers around X: ", g.BFS_layers(v2))

print(f"The distance between {v1} and {v2}:  {find_a_shortest_path(g, v1, v2)[1]}")
print(f"A shortest path between {v1} and {v2}:  {find_a_shortest_path(g, v1, v2)[0]}")
g.plot_connections()
