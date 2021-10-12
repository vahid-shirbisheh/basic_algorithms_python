from binarysearchtree import BinarySearchTree


bst = BinarySearchTree(8)
print(f"The height of the tree is {bst.height}.       The size of the tree is {bst.size}")

bst.insert(10)
print(f"The height of the tree is {bst.height}.       The size of the tree is {bst.size}")

bst.insert(7)
print(f"The height of the tree is {bst.height}.       The size of the tree is {bst.size}")
