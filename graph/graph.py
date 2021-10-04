import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def all_edges(self):
        temp = []
        previous_vertecies = []
        for vertex in self.adj_list.keys():
            previous_vertecies.append(vertex)
            connected_edges = [[vertex, tail] for tail in self.adj_list[vertex] if tail not in previous_vertecies]
            temp = temp + connected_edges
        return temp

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.all_edges())
        nx.draw_networkx(G)
        plt.show()


