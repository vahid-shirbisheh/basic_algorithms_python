import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter


class Graph:
    """
    In this class, we implement basic operation of graphs as a data structure.
    We also add several other methods useful for working with graphs.
    We allow multi edges between two vertices and loops.
    We use networkx package to visualize graphs and demonstrate our constructions.
    The methods we have already implemented are as follows:
    ♥   "__init__()" It initializes an empty graph.
    ♥   "add_vertex(vertex)"
    ♥   "__copy__()" It make a copy of the graph
    ♥   "add_edge(x, y)"
    ♥   "from_edge_list(edge_list)" It builds a graph (or expands a non-empty graph) using the list of edges of a graph
         by adding appropriate vertices and edges to the empty graph (or to the non-empty graph).
    ♥   "get_edge_list()" returns the list of all edges of the graph used to call this method.
    ♥   "__eq__(self, other)" overloads the == operator. In other words it defines the equality of two graphs.
    ♥   "__add__(self, other)" overloading the + operator. In fact this function merges two graphs.
         That is it does not repeat the common vertices and edges.
    ♥   "plot_connections()" It plots the graph object using functions and methods of networkx and matplotlib.
         It does not draw the parallel edges and loops!
    ♥   "remove_edge(x, y)" removes the edge xy if it exists
    ♥   "remove_vertex(x)" If x is a vertex, this method removes all edges incident to x and then removes x.
    ♥   "add_disconnected_graph(other)" adds two disconnected (with no common vertex) graphs.
         This method is faster and more straightforward that __add__ method.
    ♥   "BFS_layers(vertex)" It returns a list of the list of vertices ordered by layers coming from
         the Breadth-First Search strategy. It can be used in a connected graph to compute the distance of two vertices
         in linear time with respect to the number of vertices and edges.
    ♥   "connected_components()" This method returns a list of connected graphs.
    ♥   "remove_loops()" This method removes all loops and returns the resulting graph.

    Dependencies:
    Besides matplotlib.plot and networkx we have used the following functions:
    - The function merge_lists is a little function that we use to merge two graphs.
    - To compare the lists of edges of two graphs in order to check their equality,
    we have used Counter() function from Collections.
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
            if x != y:
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

    def __copy__(self):
        temp = Graph()
        temp.adj_list = self.adj_list.copy()
        return temp

    def __add__(self, other):
        temp = self.__copy__()
        for vertex in other.adj_list.keys():
            if vertex in temp.adj_list.keys():
                temp.adj_list[vertex] = merge_lists(temp.adj_list[vertex], other.adj_list[vertex])
            else:
                temp.adj_list[vertex] = other.adj_list[vertex]
        return temp

    def add_disconnected_graph(self, other):
        temp = Graph()
        temp.adj_list = merge_dicts(self.adj_list, other.adj_list)
        return temp

    def plot_connections(self):  # does not plot loops and parallel edges
        gr = nx.Graph()
        gr.add_edges_from(self.get_edge_list())
        nx.draw_networkx(gr)
        plt.show()

    def remove_edge(self, x, y):
        if x == y and x in self.adj_list.keys():  # to take care of loops
            self.adj_list[x].remove(y)
            return True
        if x in self.adj_list.keys() and y in self.adj_list.keys():
            self.adj_list[x].remove(y)
            self.adj_list[y].remove(x)
            return True
        return False

    def remove_loops(self):
        """
        Since we allowed loops and loops make problems for Breath-First Search algorithm, we define this method to
        get id of all loops in a graph before applying the BFS.
        """
        g = self.__copy__()
        for x in self.adj_list.keys():
            g.adj_list[x] = removeAll(g.adj_list[x], x)
        return g

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for tail in self.adj_list[vertex]:  # This deletes all edges incident to the vertex
                while vertex in self.adj_list[tail]:  # This takes care of possibly parallel edges
                    self.adj_list[tail].remove(vertex)
            del self.adj_list[vertex]  # This deletes the vertex
            return True
        return False

    # noinspection SpellCheckingInspection
    def BFS_layers(self, vertex):
        # In this method the graph is assumed to be connected.
        n = len(self.adj_list.keys())
        layers = [[vertex]]
        explored = [vertex]
        exploredq = Queue(vertex)
        current_layer = 0
        while len(explored) < n:
            new_layer = []
            for _ in range(len(layers[current_layer])):
                v = exploredq.dequeue()
                if v:
                    v_incidents = self.adj_list[v]
                    for other_vertex in v_incidents:
                        if other_vertex not in explored:
                            explored.append(other_vertex)
                            new_layer.append(other_vertex)
                            exploredq.enqueue(other_vertex)
            layers.append(new_layer)
            current_layer += 1
        return [layer for layer in layers if len(layer) > 0]

    def connected_components(self):
        components = []
        explored = []
        for vertex in self.adj_list.keys():
            if vertex not in explored:
                explored.append(vertex)
                current_queue = Queue(vertex)
                new_component = Graph()
                new_component.add_vertex(vertex)
                new_component.adj_list[vertex] = self.adj_list[vertex]
                while current_queue.length > 0:
                    vertex = current_queue.dequeue()
                    for other_vertex in self.adj_list[vertex]:
                        if other_vertex not in explored:
                            explored.append(other_vertex)
                            current_queue.enqueue(other_vertex)
                            new_component.add_vertex(other_vertex)
                            new_component.adj_list[other_vertex] = self.adj_list[other_vertex]
                components.append(new_component)
        return components


def merge_lists(list1, list2):
    temp1 = list1[:]
    temp2 = [x for x in list2 if x not in list1]
    temp1.extend(temp2)
    return temp1


def merge_dicts(dict1, dict2):
    temp = dict1.copy()
    for d in dict2:
        if d not in temp:
            temp[d] = dict2[d]
    return temp


def removeAll(my_list, elt):
    temp = []
    for x in my_list:
        if x != elt:
            temp.append(x)
    return temp


"""
Here we build queue class to use in Breadth-First Search.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self, *args):
        # Unifying all variety of input arguments as lists
        args_list = []
        if len(args) == 0 or args[0] is None:  # no argument or None as the argument
            pass
        elif len(args) == 1:
            if type(args[0]) != list:  # one argument and it is not a list
                if type(args[0]) == range:
                    args_list = list(args[0])
                else:
                    args_list = list([args[0]])
            else:  # one argument and it is a list
                args_list = args[0]
        else:
            args_list = list(args)  # several arguments and they are list or not-list

        self.length = len(args_list)  # Setting the length of the queue object

        # constructing a queue according to the length of args_list
        if len(args_list) == 0:  # zero-length or empty queue
            self.first = None
            self.last = None
        elif len(args_list) == 1:  # queue with one element
            new_node = Node(args_list[0])
            self.first = new_node
            self.last = new_node
        else:  # queue with multiple elements
            node_temp = Node(args_list[0])
            self.first = node_temp
            for i in range(1, len(args_list)):
                new_node = node_temp
                node_temp = Node(args_list[i])
                new_node.next = node_temp
            self.last = node_temp

    def __eq__(self, other):
        """
        Since we are going to use this method for testing the functionality of other methods,
        we do not assume all objects were constructed correctly. So, we intentionally double check
        the validity of construction of objects.
        """
        if self.length != other.length:
            return False
        else:
            if self.length == 0:
                return self.first is None and other.first is None
            elif self.length == 1:
                return self.first.value == other.first.value and self.last.value == other.last.value
            else:
                temp1 = self.first
                temp2 = other.first
                while temp1:
                    if not (temp1.value == temp2.value):
                        return False
                    temp1 = temp1.next
                    temp2 = temp2.next
                return True

    def __str__(self):
        temp_string = "(first)"
        temp = self.first
        while True:
            if temp:
                temp_string = temp_string + str(temp.value)
            else:
                temp_string = temp_string + str(temp)
            if temp == self.last:
                temp_string = temp_string + "(last)"
                break
            else:
                temp_string = temp_string + " -> "
            temp = temp.next
        if self.length > 0:
            temp_string = temp_string + " -> None"
        return temp_string

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        self.first = temp.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return temp.value
