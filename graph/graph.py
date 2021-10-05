import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

"""
In this class, we implement basic operation of graphs as a data structure. 
We also add several other methods useful for working with graphs.
We use networkx package to visualize graphs and demonstrate our constructions.
The methods we have already implemented are as follows:
♥   "__init__()" It initializes an empty graph.
♥   "add_vertex(vertex)"
♥   "add_edge(x, y)"
♥   "from_edge_list(edge_list)" It builds a graph using the list of edges of a graph by adding 
    appropriate vertices and edges to an empty graph.
♥   "get_edge_list()" returns the list of all edges of the graph used to call this method.
♥   "__eq__(self, other)" overloads the == operator. In other words it defines the equality of two graphs.
♥   "__add__(self, other)" overloading the + operator. In fact this function merges two graphs. 
    That is it does not repeat the common vertices and edges. 
♥   "plot_connections()" It plots the graph object using functions and methods of networkx and matplotlib.
    It does not draw the parallel edges and loops!
♥   
♥   
♥   
♥   

Dependencies:
Besides matplotlib.plot and networkx we have sed the following functions:
The function merge is a little function that we use to merge two graphs. To compare the lists of edges of two graphs 
in order to check their equality, we have used Counter() function from Collections.    
"""


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, x, y):
        if x == y and x in self.adj_list.keys():  # to take care of loops
            self.adj_list[x].append(y)
            return True
        if x in self.adj_list.keys() and y in self.adj_list.keys():
            self.adj_list[x].append(y)
            self.adj_list[y].append(x)
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
            self.adj_list[y].append(x)

    def get_edge_list(self):
        temp = []
        previous_vertices = []
        for vertex in self.adj_list.keys():
            connected_edges = [[vertex, tail] for tail in self.adj_list[vertex] if tail not in previous_vertices]
            previous_vertices.append(vertex)
            temp = temp + connected_edges
        return temp

    def __eq__(self, other):
        if set(self.adj_list.keys()) != set(other.adj_list.keys()):
            return False
        else:
            for vertex in self.adj_list.keys():
                if Counter(self.adj_list[vertex]) != Counter(other.adj_list[vertex]):
                    return False
        return True

    def __add__(self, other):
        temp = Graph()
        temp.from_edge_list(merge(self.get_edge_list(), other.get_edge_list()))
        return temp

    def plot_connections(self):  # does not plot loops and parallel edges
        gr = nx.Graph()
        gr.add_edges_from(self.get_edge_list())
        nx.draw_networkx(gr)
        plt.show()


def merge(list1, list2):
    temp1 = list1[:]
    temp2 = [x for x in list2 if x not in list1]
    temp1.extend(temp2)
    return temp1
