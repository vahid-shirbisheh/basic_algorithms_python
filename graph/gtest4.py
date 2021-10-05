from graph import Graph

"""
to demonstrate how to merge two graphs using overloading + operator 
"""
g1 = Graph()
g2 = Graph()

g1.from_edge_list([['A', 'B'], ['B', 'C'], ['C', 'A']])
g2.from_edge_list([['A', 'D'], ['D', 'E'], ['A', 'E']])

# different representations
print("The graph g1 as a dictionary:\n", g1.adj_list)
print("The graph g1 as a list of edges:\n", g1.get_edge_list())
print("The graph g2 as a dictionary:\n", g2.adj_list)
print("The graph g2 as a list of edges:\n", g2.get_edge_list())
g3 = g1 + g2
print("The graph g3 as a dictionary:\n", g3.adj_list)
print("The graph g3 as a list of edges:\n", g3.get_edge_list())

g3.plot_connections()
