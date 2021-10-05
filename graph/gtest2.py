from graph import Graph

# A disconnected graph is plotted!
g1 = Graph()
a, b, c, d, e, f = "A", "B", "C", "D", "E", "F"
g1.add_vertex(a)
g1.add_vertex(b)
g1.add_vertex(c)
g1.add_vertex(d)
g1.add_vertex(e)
g1.add_vertex(f)

g1.add_edge(a, c)
g1.add_edge(a, b)
g1.add_edge(b, c)
g1.add_edge(e, d)
g1.add_edge(d, f)
g1.add_edge(e, f)

# different representations
print("The graph as a dictionary:\n", g1.adj_list)
print("The graph as a list of edges:\n", g1.get_edge_list())
g1.plot_connections()


