class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
In the following, we construct a class for LinkedList with an initializer (constructor) 
that accepts various types of arguments such as None, empty (no argument), lists, tuples, etc. 
We are going to add a number of methods, listed below, to our class to enhance our further experiences:
♥   __eq__   defines when two linkedlists are equal (==)
♥   __str__  returns a string representation of the linkedlist (equivalent of toString() method in Java classes)
♥   append(x)
♥   pop()
♥   prepend(value)
♥   popFirst()
♥   toList() returns a list made up by values of the linkedlist
♥   insert(index, value) inserts a node with this value at the index
♥   remove(index) removes the node at the mentioned index
♥   get(index) gets the value of the node at the index
♥   set(index, value) sets the value in the node at the index
♥   slice(start, end=-1)   returns a slice of the linkedlist according to 
♥   pos(value) returns the index of the first value in the linkedlist equal to x, otherwise returns False
♥   __add__ overloading + operator for linkedlists
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
                if type(args[0]) == range:
                    args_list = list(args[0])
                else:
                    args_list = list([args[0]])
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
        return True

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

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

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

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        after = temp.next
        new_node = Node(value)
        temp.next = new_node
        new_node.next = after
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop()
        before = self.head
        for _ in range(index - 1):
            before = before.next
        temp = before.next
        after = temp.next
        before.next = after
        self.length -= 1
        temp.next = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp.value

    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next
        temp.value = value
        return True

    def slice(self, start, end=0):
        while end <= 0:
            end += self.length
        while start < 0:
            start += self.length
        if end > self.length:
            end = self.length
        if start > end or start > self.length:
            return None
        temp = LinkedList()
        for index in range(start, end):
            temp.append(self.get(index))
        return temp

    def pos(self, value):
        if self.length == 0:
            return False
        i = False
        temp = self.head
        for j in range(self.length):
            if value == temp.value:
                i = j
                break
            temp = temp.next
        return i

    def __add__(self, other):
        if other.length == 0:
            return self
        if self.length == 0:
            return other
        temp1 = self.slice(0)
        temp2 = other.head
        while temp2:
            temp1.tail.next = temp2
            temp1.tail = temp2
            temp1.length += 1
            temp2 = temp2.next
        temp1.tail.next = temp2
        return temp1
