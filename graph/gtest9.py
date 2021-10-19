from graph import Graph

"""
to test the method remove_loops()
"""

g = Graph()
g.from_edge_list([['A', 'A'], ['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['B', 'E'],
                  ['P', 'P'], ['P', 'P'], ['P', 'P'], ['Q', 'Q'], ['P', 'Q'],
                  ['H', 'H']])
print("The graph g as a list of edges:\n", g.get_edge_list())
print("The graph g as a dictionary:\n", g.adj_list)

g = g.remove_loops()
print("\n   ***   After removing all loops   ***\n")
print("The graph g as a list of edges:\n", g.get_edge_list())
print("The graph g as a dictionary:\n", g.adj_list)
