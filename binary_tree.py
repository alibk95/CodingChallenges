# 17
# Binary tree implementation
class Node:
    def __init__(self, value=None):
        self.value = value
        self.right_child = None
        self.left_child = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value is already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height + 1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def find(self, value):
        if self.root != None:
            return self._find(value, self.root)
        else:
            return 0

    def _find(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find(value, cur_node.right_child)
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find(value, cur_node.left_child)
        else:
            return False

# Code driver 17
tree = BinarySearchTree()
# init the binary search tree
tree.insert(5)
tree.insert(1)
tree.insert(3)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.insert(0)
tree.insert(20)
# print the tree
tree.print_tree()
print("The height of the tree is: ",tree.height())
print("If the value you are looking for exist or not: ", tree.find(30))