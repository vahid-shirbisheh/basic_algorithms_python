"""
Here we build queue class using linkedlist class. Afterwards we will build queue class independently.
"""
import sys
sys.path.append('C:\\Users\\acer\\basic_algorithms_python\\linked_list')
from linkedlist import LinkedList


class Queuell:
    def __init__(self, *args):
        self.body = LinkedList(*args)
        self.first = self.body.head
        self.last = self.body.tail
        self.length = self.body.length

    def __eq__(self, other):
        return self.body == other.body

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
        self.body.append(value)
        self.last = self.body.tail
        if self.length == 0:
            self.first = self.body.head
        self.length += 1
        return True

    def dequeue(self):
        temp = self.body.popFirst()
        if self.length > 0:
            self.length -= 1
            self.first = self.body.head
            if self.length == 0:
                self.last = self.body.tail  # which is equal to None
            temp = temp.value
        return temp
