from graph import Graph

"""
removing edges and vertices 
Note that when removing the vertex A, both parallel edges between A and C are removed! 
"""

edges = [["A", "B"], ["B", "C"], ["C", "A"], ["A", "D"], ["D", "C"], ["C", "A"], ["B", "D"]]
g1 = Graph()
g1.from_edge_list(edges)

# different representations
print("The graph g1 as a list of edges:\n", g1.get_edge_list())
# removing the edge BC
g1.remove_edge('B', 'C')
print("The graph g1 after removing the edge BC:\n", g1.get_edge_list())
# removing the vertex A
g1.remove_vertex('A')
print("The graph g1 after removing the vertex A:\n", g1.get_edge_list())
# Although, the graph g1 is not empty, we can add the edges from a list and expand the graph
g1.from_edge_list([["U", "W"], ["W", "Z"], ["Z", "B"], ["W", "D"]])
print("The graph g1 after a list of new edges:\n", g1.get_edge_list())
g1.plot_connections()