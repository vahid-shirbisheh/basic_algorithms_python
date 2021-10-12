from binarysearchtree import BinarySearchTree


bst = BinarySearchTree()
my_list = [10, 14, 3, 4, 18, 11, 9, 20, 15, 2]
bst.fromList(my_list)
print(f"The height of the tree is {bst.height}        The size of the tree is {bst.size} ")
