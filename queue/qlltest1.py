from queuell import *

print("      *** Different versions of empty queue *** ")
qll_empty = Queuell()
qll_none = Queuell(None)
qll_bracket = Queuell([])
print(qll_empty, qll_none, qll_bracket, "\nWhether qll_empty == qll_none? ", qll_empty == qll_none)
print("      *** Comparing with the linkedlist inside the queue *** ")
qll = Queuell(1)
print(qll)
print(qll.body)
print("      *** from lists and range *** ")
qll1 = Queuell([2, 4, 6])
qll2 = Queuell(range(2, 8, 2))
print(qll1 == qll2)
print(qll2)
print("      *** enqueue *** ")
qll1 = Queuell(1, 2, 3)
qll1.enqueue(4)
print(qll1.first.value)
print(qll1.last.value)
print(qll1)
qll2 = Queuell(1, 2, 3, 4)
print(qll1 == qll2)
print("      *** enqueue the first element *** ")
qll1 = Queuell()
qll1.enqueue("The first element")
print(qll1.first.value)
print(qll1.last.value)
print(qll1)
qll2 = Queuell("The first element")
print(qll1 == qll2)
print("      *** dequeue *** ")
qll1 = Queuell(1, 2, 3, 4)
print(qll1.dequeue().value)
qll2 = Queuell(2, 3, 4)
print(qll1 == qll2)
print(qll1)
print("      *** dequeue the last element *** ")
qll1 = Queuell("The last element")
qll1.dequeue()
print(qll1.first)
print(qll1.last)
print(qll1)
qll2 = Queuell()
print(qll1 == qll2)
