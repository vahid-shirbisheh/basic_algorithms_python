from graph import Graph

"""
to test the method connected_components()
"""

g = Graph()
g.from_edge_list([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['B', 'E'],
                  ['X', 'Y'], ['Y', 'Z'], ['X', 'Z'],
                  ['P', 'Q'],
                  ['H', 'H']])
print("The graph g as a list of edges:\n", g.get_edge_list(), "\n")
components = g.connected_components()
for graph in components:
    print(graph.get_edge_list())
g.plot_connections()
