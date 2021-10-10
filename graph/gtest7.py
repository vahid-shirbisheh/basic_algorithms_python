from graph import Graph

"""
to test the fact that the method __copy__() makes a copy of the object graph
"""

g1 = Graph()
g1.from_edge_list([['A', 'B'], ['B', 'C'], ['C', 'A']])
g2 = g1.__copy__()
print(g1 == g2)
g1.add_vertex("K")
g1.add_edge("A", "K")
print("The graph g1 as a dictionary:\n", g1.adj_list)
print("The graph g1 as a list of edges:\n", g1.get_edge_list())
print("The graph g2 as a dictionary:\n", g2.adj_list)
print("The graph g2 as a list of edges:\n", g2.get_edge_list())
print(g1 == g2)
