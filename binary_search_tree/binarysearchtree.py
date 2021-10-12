class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self, value=None):
        if value:
            new_node = Node(value)
            self.root = new_node
            self.size = 1  # the number of nodes in the tree
            self.height = 1  # the number of layers in the tree
        else:
            self.root = None
            self.size = 0
            self.height = 0

    def insert(self, value):
        if value is None:
            return False
        self.size += 1
        new_node = Node(value)
        if self.size == 0:
            self.root = new_node
            self.height += 1
            return True
        temp_height = 1
        temp = self.root
        temp_2 = temp
        direction = None
        while temp:
            temp_2 = temp
            if temp.value < value:
                temp = temp_2.right
                direction = True  # By convention "True" direction is towards right
                temp_height += 1
            elif temp.value > value:
                temp = temp_2.left
                direction = False  # By convention "False" direction is towards left
                temp_height += 1
            else:
                self.size -= 1
                return False
        if direction:
            temp_2.right = new_node
        else:
            temp_2.left = new_node
        self.height = max(temp_height, self.height)
        return True
