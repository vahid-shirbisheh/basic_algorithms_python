import sys
sys.path.append('C:\\Users\\acer\\basic_algorithms_python\\graph')

from graph import Graph


"""
Here, we implement a function to construct a grid.
"""


def grid(m, n):
    graph = Graph()
    for i in range(0, m):
        for j in range(0, n):
            graph.add_vertex((i, j))

    for i in range(0, m - 1):
        for j in range(0, n - 1):
            graph.add_edge((i, j), (i, j+1))
            graph.add_edge((i, j), (i+1, j))
        graph.add_edge((i, n-1), (i + 1, n-1))

    for j in range(0, n - 1):
        graph.add_edge((m-1, j), (m-1, j + 1))
    return graph


g = grid(3, 5)
v0 = (0, 0)
print(f"Layers around the vertex {v0}")
layers = g.BFS_layers(v0)
for layer in layers:
    print(layer)

print(f"Depth-First Search starting from the vertex {v0}")

print(g.depth_first_search(v0))
g.plot_connections()
