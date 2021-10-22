import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter


class DiGraph:
    """
    In this class, we implement basic operation of directed graphs as a data structure.
    We allow multiple parallel edges and loops.
    We also add several other methods useful for working with directed graphs.
    We use networkx package to visualize digraphs and demonstrate our constructions.
    The methods we have already implemented are as follows:
    ♥   "__init__()" It initializes an empty digraph.
    ♥   "add_vertex(vertex)"
    ♥   "add_edge(x, y)"
    ♥   "from_edge_list(edge_list)" It builds a digraph (or expands a non-empty digraph) using the list of edges
        by adding appropriate vertices and edges to the empty (non-empty) digraph.
    ♥   "get_edge_list()" returns the list of all edges of the digraph object.
    ♥   "__eq__(self, other)" overloads the == operator. In other words it defines the equality of two graphs.
    ♥   "__add__(self, other)" overloading the + operator. In fact this function merges two graphs.
        That is it does not repeat the common vertices and edges.
    ♥   "plot_connections()" It plots the digraph object using functions and methods of networkx and matplotlib.
        It does not draw the parallel edges and loops!
    ♥   "remove_edge(x, y)" removes the edge xy if it exists
    ♥   "remove_vertex(x)" If x is a vertex, this method removes all edges originating from x and then removes x.
    ♥
    ♥
    ♥

    Dependencies:
    Besides matplotlib.plot and networkx we have used the following functions:
    The function merge is a little function that we use to merge two graphs. To compare the lists of edges of two graphs
    in order to check their equality, we have used Counter() function from Collections.
    """

    def __init__(self):
        self.adj_list = {}

    def __str__(self):
        return str(self.adj_list)

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, x, y):
        if x in self.adj_list.keys() and y in self.adj_list.keys():
            self.adj_list[x].append(y)
            return True
        return False

    def from_edge_list(self, edge_list):
        for [x, y] in edge_list:
            # adding the vertices
            if x not in self.adj_list.keys():
                self.adj_list[x] = []
            if y not in self.adj_list.keys():
                self.adj_list[y] = []
            # adding the edges
            self.adj_list[x].append(y)
