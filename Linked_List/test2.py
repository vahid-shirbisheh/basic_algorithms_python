from linkedlist import LinkedList

print("*** casting linkedlists to python lists: ***")
ll = LinkedList(1, 4, 3, "book")
ll.append("Kite")
print(type(ll), ll)
l = ll.toList()
print(type(l), l)
