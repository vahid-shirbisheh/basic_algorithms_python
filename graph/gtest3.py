from graph import Graph

"""
to test the equality of two graphs
"""
g1 = Graph()
g2 = Graph()

a, b, c, d = "A", "B", "C", "D"
g1.add_vertex(a)
g1.add_vertex(b)
g1.add_vertex(c)
g1.add_vertex(d)

g1.add_edge(a, d)
g1.add_edge(a, b)
g1.add_edge(b, c)
g1.add_edge(b, d)

g2.from_edge_list([['A', 'D'], ['A', 'B'], ['B', 'C'], ['B', 'D']])

# different representations
print("The graph g1 as a dictionary:\n", g1.adj_list)
print("The graph g1 as a list of edges:\n", g1.get_edge_list())
print("The graph g2 as a dictionary:\n", g2.adj_list)
print("The graph g2 as a list of edges:\n", g2.get_edge_list())
print("Whether g1 == g2? ", g1 == g2)

g2.plot_connections()
