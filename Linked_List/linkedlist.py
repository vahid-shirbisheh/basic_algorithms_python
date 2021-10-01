class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
In the following we construct a class for LinkedList with a initializer (constructor) 
that accepts various types of arguments such as None, empty (no argument), lists, tuples, etc. 
We are going to add a number of methods, listed below, to our class to enhance our further experiences:
♥   __eq__   to define when two linkedlists are equal (==)
♥   __str__  to return a string representation of the linkedlist (equivalent of toString() method in Java classes)
♥   append(x)
♥   pop()
♥   prepend()
♥   popFirst(value)
♥   slice(start, end=-1)   returns a slice of the linkedlist according to 
♥   pos(value) returns the index of the first value in the linkedlist equal to x, otherwise returns False
♥   insert(value, index) inserts the value in the index
♥   remove(index)
♥   toList() returns a list made up by values of the linkedlist
♥   
♥   
♥   
♥   
♥   
♥   
♥   
"""


class LinkedList:
    def __init__(self, *args):
        # Unifying all variety of input arguments as lists
        args_list = []
        if len(args) == 0 or args[0] is None:  # no argument or None as the argument
            pass
        elif len(args) == 1:
            if type(args[0]) != list:  # one argument and it is not a list
                args_list = list([args0])
            else:  # one argument and it is a list
                args_list = args[0]
        else:
            args_list = list(args)  # several arguments and they are list or not-list

        self.length = len(args_list)  # Setting the length of the linkedlist object

        # constructing a linkedlist according to the length of args_list
        if len(args_list) == 0:  # length zero or empty linkedlist
            self.head = None
            self.tail = None
        elif len(args_list) == 1:  # linkedlist with one element
            new_node = Node(args_list[0])
            self.head = new_node
            self.tail = new_node
        else:  # linkedlist with multiple elements
            node_temp = Node(args_list[0])
            self.head = node_temp
            for i in range(1, len(args_list)):
                new_node = node_temp
                node_temp = Node(args_list[i])
                new_node.next = node_temp
            self.tail = node_temp

    def __eq__(self, other):
        if self.length != other.length:
            return False
        else:
            if self.length == 0:
                return self.head is None and other.head is None
            elif self.length == 1:
                return self.head.value == other.head.value and self.tail.value == other.tail.value
            else:
                temp1 = self.head
                temp2 = other.head
                while temp1:
                    if not (temp1.value == temp2.value):
                        return False
                    temp1 = temp1.next
                    temp2 = temp2.next
                return True

    def __str__(self):
        temp_string = "(head)"
        temp = self.head
        while True:
            if temp:
                temp_string = temp_string + str(temp.value)
            else:
                temp_string = temp_string + str(temp)
            if temp == self.tail:
                temp_string = temp_string + "(tail)"
                break
            else:
                temp_string = temp_string + " -> "
            temp = temp.next
        if self.length > 0:
            temp_string = temp_string + " -> None"
        return temp_string

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        temp1 = self.head
        temp2 = self.head
        while temp1.next:
            temp2 = temp1
            temp1 = temp1.next
        self.tail = temp2
        self.tail.next = None
        self. length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp1

    def toList(self):
        temp = []
        if self.length == 0:
            return temp
        else:
            element = self.head
            temp.append(element.value)
            while element.next:
                element = element.next
                temp.append(element.value)
            return temp
