
from graph import Graph


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
my_graph.add_edge(a, d)
my_graph.add_edge(d, f)
my_graph.add_edge(b, c)
my_graph.add_edge(b, d)
my_graph.add_edge(e, c)
my_graph.add_edge(e, b)
my_graph.add_edge(e, f)
my_graph.add_edge(i, g)
my_graph.add_edge(g, h)
my_graph.add_edge(i, h)
my_graph.add_edge(f, i)
my_graph.add_edge(g, b)

# different representations
print(my_graph.adj_list)
my_graph.print_graph()
print(my_graph.all_edges())
my_graph.visualize()
