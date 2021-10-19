from graph import Graph

"""
to test the method connected_components()
"""

g = Graph()
g.from_edge_list([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['B', 'E'],
                  ['X', 'Y'], ['Y', 'Z'], ['X', 'Z'],
                  ['P', 'Q'],
                  ['H', 'H']])
# To test if the method connected_components() works correctly in the presence of loops add the following two edges:
g.add_edge('A', 'A')
g.add_edge('X', 'X')
"""
"""
print("The graph g as a list of edges:\n", g.get_edge_list(), "\n")
components = g.connected_components()
for graph in components:
    print(graph.get_edge_list())
g.plot_connections()
