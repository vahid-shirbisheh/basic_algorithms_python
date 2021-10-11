"""
Here we build queue class independent of linkedlist class.
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
