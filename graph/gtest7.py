from graph import Graph

"""
to test the equality of two graphs
"""

g1 = Graph()
g1.from_edge_list([['A', 'B'], ['B', 'C'], ['C', 'A']])
g2 = g1.copy()
print(g1 == g2)
