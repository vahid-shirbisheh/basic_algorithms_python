from graph import Graph


"""
To test depth_first_search method
"""


g = Graph()
g.from_edge_list([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['B', 'E'], ['E', 'Y'],
                  ['X', 'Y'], ['Y', 'Z'], ['X', 'Z'],
                  ['P', 'Q'], ['Q', 'M'], ['M', 'N'], ['N', 'Q'], ['P', 'E'],
                  ['H', 'M']])

print("The graph g as a list of edges:\n", g.get_edge_list(), "\n")
print("The graph g as a dictionary:\n", g.adj_list, "\n")
# Testing the depth-first search function
print(g.depth_first_search("E"))

g.plot_connections()

