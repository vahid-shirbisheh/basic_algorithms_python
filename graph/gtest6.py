from graph import Graph


print("     *** layers around a vertex in a graph produced by the BFS (Breadth-First Search) strategy  ***       ")

g = Graph()
edges = [["H", "X"], ["U", "C"], ["C", "H"], ["W", "Z"], ["X", "V"],
         ["G", "S"], ["E", "G"], ["J", "H"], ["J", "F"], ["V", "Z"],
         ["X", "E"], ["U", "W"], ["S", "F"], ["A", "F"], ["W", "X"]]
g.from_edge_list(edges)

print(g)

print("The list of layers around X: ", g.BFS_layers("X"))
print("The list of layers around Z: ", g.BFS_layers("Z"))
print("The list of layers around A: ", g.BFS_layers("A"))
print("The list of layers around H: ", g.BFS_layers("H"))

g.plot_connections()
