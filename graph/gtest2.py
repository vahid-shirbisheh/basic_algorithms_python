from graph import Graph


g1 = Graph()
a, b, c, d = "A", "B", "C", "D"
g1.add_vertex(a)
g1.add_vertex(b)
g1.add_vertex(c)
g1.add_vertex(d)

g1.add_edge(a, a)
g1.add_edge(a, b)
g1.add_edge(b, c)
g1.add_edge(c, d)
g1.add_edge(d, b)

# different representations
print("The graph as a dictionary:\n", g1.adj_list)
print("The graph as a list of edges:\n", g1.get_edge_list())
g1.plot_connections()
