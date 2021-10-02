from linkedlist import LinkedList

# This is how to implement linkedlist comprehension:
ll = LinkedList(range(10))
llc = LinkedList([x * 5 for x in ll.toList() if x % 3 == 0])
print(llc)
