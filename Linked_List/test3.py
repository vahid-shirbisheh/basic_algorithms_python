from linkedlist import LinkedList

print("*** get: ***")
ll = LinkedList(1, 4, 3, "book")
print(ll.get(2))
print(ll.get(-1))
print(ll.get(4))

print("*** set: ***")
ll.set(2, "flower")
print(ll)
print(ll.set(6, 8))

print("*** slice: ***")
ll = LinkedList(range(10))
print(ll)
sll = ll.slice(2, 8)
print("slice of ll from 2 to 8:     ", sll, "    length of the slide = ", sll.length)
sll = ll.slice(-2, -1)
print("slice of ll from -2=10-2=8 to -1=10-1=9:     ", sll, "    length of the slide = ", sll.length)
sll = ll.slice(-4)
print("slice of ll from -4=10-4=6 to 0=10-0=10:     ", sll, "    length of the slide = ", sll.length)

print("*** index: ***")
print(ll)
print("index of 0 = ", ll.index(0))
print("index of 3 = ", ll.index(3))
print("index of 9 = ", ll.index(9))
print("index of 23 = ", ll.index(23))

print("*** adding two linkedlists sing __add__ (overloading the + operator): ***")
ll1 = LinkedList(range(3))
ll2 = LinkedList(range(3, 11))
ll3 = ll1 + ll2
ll4 = LinkedList(range(11))
print(ll3 == ll4)
print(ll3)
print(LinkedList() + ll1)
print(ll1 + LinkedList())
print(LinkedList() + LinkedList())

print("*** reverse: ***")
ll = LinkedList("horse", "dog", "cat")
print(ll)
print(ll.reverse())
ll = LinkedList(range(6))
print(ll)
print(ll.reverse())
