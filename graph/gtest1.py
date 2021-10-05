from graph import Graph

"""
checks the basic construction of a graph and how to view it as a dictionary, a list of edges, and pictorial.
"""
my_graph = Graph()
a, b, c, d, e, f, g, h, i = "A", "B", "C", "D", "E", "F", "G", "H", "I"
my_graph.add_vertex(a)
my_graph.add_vertex(b)
my_graph.add_vertex(c)
my_graph.add_vertex(d)
my_graph.add_vertex(e)
my_graph.add_vertex(f)
my_graph.add_vertex(g)
my_graph.add_vertex(h)
my_graph.add_vertex(i)
my_graph.add_edge(a, b)
my_graph.add_edge(a, c)
my_graph.add_edge(f, c)
my_graph.add_edge(b, d)
my_graph.add_edge(e, c)
my_graph.add_edge(e, b)
my_graph.add_edge(e, f)
my_graph.add_edge(g, h)
my_graph.add_edge(d, h)
my_graph.add_edge(f, i)
my_graph.add_edge(g, b)

# different representations
print("The graph as a dictionary:\n", my_graph.adj_list)
print("The graph as a list of edges:\n", my_graph.get_edge_list())
my_graph.plot_connections()
