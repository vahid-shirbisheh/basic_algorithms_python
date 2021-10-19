from graph import Graph

# noinspection SpellCheckingInspection
"""
To test whether our implementation of BFS works fine with the present of loops.
Compare this test with gtest.py
"""

print('     *** layers around a vertex in a graph "with loops" produced by the BFS strategy  ***')

g = Graph()
edges = [["X", "X"], ["H", "X"], ["U", "C"], ["C", "H"], ["W", "Z"], ["X", "V"],  # We added a loop at X
         ["G", "S"], ["E", "G"], ["J", "H"], ["J", "F"], ["V", "Z"],
         ["A", "A"], ["A", "A"], ["X", "E"], ["U", "W"], ["S", "F"], ["A", "F"], ["W", "X"]]  # We added two loops at A
g.from_edge_list(edges)

print(g)

print("The list of layers around X: ", g.BFS_layers("X"))
print("The list of layers around Z: ", g.BFS_layers("Z"))
print("The list of layers around A: ", g.BFS_layers("A"))
print("The list of layers around H: ", g.BFS_layers("H"))

g.plot_connections()
