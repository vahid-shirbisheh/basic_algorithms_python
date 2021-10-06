import sys
sys.path.append('C:\\Users\\acer\\basic_algorithms_python\\linked_list')
from linkedlist import LinkedList


class Node:
    def __init__(self, value):
        self.value = value
        self.down = None


"""
In the following, we construct a class for stacks with an initializer (constructor) 
that accepts various types of arguments such as None, empty (no argument), lists, tuples, etc. 
We are going to add the following methods to our class to enhance our further experiences:
♥   push(x)
♥   pop()
♥   toList() returns a list made up by values of the stack
♥   toLinkedList() returns a linkedlist made up by values of the stack
♥   __str__  returns a string representation of the stack (equivalent of toString() method in Java classes)
♥   __eq__   defines when two stacks are equal (==)
"""


class Stack:
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

        self.height = len(args_list)  # Setting the height of the stack

        # constructing a stack according to the length of args_list
        if len(args_list) == 0:  # height zero or empty stack
            self.top = None
        elif len(args_list) == 1:  # stack with one element
            new_node = Node(args_list[0])
            self.top = new_node
        else:  # stack with multiple elements
            node_temp = Node(args_list[0])
            self.top = node_temp
            for i in range(1, len(args_list)):
                new_node = Node(args_list[i])
                new_node.down = node_temp
                node_temp = new_node
                self.top = node_temp

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
            self.height += 1
            return True
        new_node.down = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.down
        temp.down = None
        self.height -= 1
        return temp.value

    def toList(self):
        temp = []
        if self.height == 0:
            return temp
        temp_node = self.top
        while temp_node:
            temp.append(temp_node.value)
            temp_node = temp_node.down
        temp.reverse()
        return temp

    def toLinkedList(self):
        temp = LinkedList()
        if self.height == 0:
            return temp
        temp_node = self.top
        while temp_node:
            temp.append(temp_node.value)
            temp_node = temp_node.down
        return temp

    def __str__(self):
        temp_string = "(top)"
        temp = self.top
        while temp:
            if temp:
                temp_string = temp_string + str(temp.value)
            else:
                temp_string = temp_string + str(temp)
            temp_string = temp_string + " -> "
            temp = temp.down
        if self.height > 0:
            temp_string = temp_string + "None"
        return temp_string

    def __eq__(self, other):
        if self.height != other.height:
            return False
        temp1 = self.top
        temp2 = other.top
        while temp1:
            if temp1.value != temp2.value:
                return False
            temp1 = temp1.down
            temp2 = temp2.down
        return temp1 == temp2


