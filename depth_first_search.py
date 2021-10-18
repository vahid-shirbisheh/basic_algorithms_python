import sys
sys.path.append('C:\\Users\\acer\\basic_algorithms_python\\graph')
sys.path.append('C:\\Users\\acer\\basic_algorithms_python\\stack')

from graph import Graph
from stack import Stack


"""
Here, we implement a Depth-First Search algorithm for undirected graphs.
"""


def dfs(graph, vertex):
    def next(v):
        temp = None
        for x in graph.adj_list[v]:
            if x not in visited_list:
                temp = x
                break
        return temp
    visited_list = [vertex]
    visited_stack = Stack(vertex)
    current_vertex = vertex
    backward = False
    i = 0  # Just to track the order of discovering new vertices
    while visited_stack.height > 0:
        i += 1
        print(i, "  Stack = ", visited_stack)  # Just to track the order of discovering new vertices
        if backward:
            current_vertex = visited_stack.pop()
        next_vertex = next(current_vertex)
        backward = False
        if next_vertex:
            if (visited_stack.top and visited_stack.top.value != current_vertex) or (visited_stack.top is None and next(current_vertex)):
                visited_stack.push(current_vertex)
            current_vertex = next_vertex
            visited_stack.push(next_vertex)
            visited_list.append(next_vertex)
        else:
            backward = True
    return visited_list


g = Graph()
g.from_edge_list([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'A'], ['B', 'E'], ['E', 'Y'],
                  ['X', 'Y'], ['Y', 'Z'], ['X', 'Z'],
                  ['P', 'Q'], ['Q', 'M'], ['M', 'N'], ['N', 'Q'], ['P', 'E'],
                  ['H', 'M']])

# Another example
"""
g.from_edge_list([['F', 'E'], ['F', 'A'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['X', 'E'], ['Z', 'E'], ['Y', 'E']])
"""
# print("The graph g as a list of edges:\n", g.get_edge_list(), "\n")
print("The graph g as a dictionary:\n", g.adj_list, "\n")
# Testing the depth-first search function
print(dfs(g, "E"))


# print("Drawing the graph!")
g.plot_connections()
