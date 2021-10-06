from stack import Stack
import sys
sys.path.append('C:\\Users\\acer\\basic_algorithms_python\\linked_list')
from linkedlist import LinkedList


"""
To test the initializer and the following methods:
1. push
2. pop
3. toList
4. toLinkedList
5. __str__
6. __eq__
"""
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(100)
print("removing 100 from the top of the stack: ", s.pop())
s.push(4)
print('The linear representation of the stack: ', s)
print('The list representation of the stack: ', s.toList())
print('The stack constructed from the list representation of the original stack: ', Stack(s.toList()))
ll = s.toLinkedList()
print('The linkedlist representation of the stack: ', ll)
print("Whether s == Stack(s.toList())? ", s == Stack(s.toList()))
print("Whether Stack([30, 40, 50]) == Stack(30, 40, 50)? ", Stack([30, 40, 50]) == Stack(30, 40, 50))
print("Whether Stack([30, 40, 50]) == Stack(30, 40, 51)? ", Stack([30, 40, 50]) == Stack(30, 40, 51))
print("Whether Stack([0, 1, 2]) == Stack(range(3))? ", Stack([0, 1, 2]) == Stack(range(3)))
print("Whether Stack() == Stack(None)? ", Stack() == Stack(None))
print("Whether Stack([]) == Stack(None)? ", Stack([]) == Stack(None))
