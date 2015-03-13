

class binaryTree:
    """
    Class binaryTree instantiates instance variable node, and two children as none.
    Places numbers as follows: if number is great than the node, places on the right, if less than places to the left.
    """
    def __init__(self, node):
        self.node = node
        self.right_child = None
        self.left_child = None

    def insert(self, node): # node is a number
        if node < self.node:  # Place left
            if self.left_child is None:  # The base case
                self.left_child = binaryTree(node)
            else:  # Else left child object exists and I need to apply insert method on left_child
                self.left_child.insert(node)  # changing state
        if node > self.node:  # Place right
            if self.right_child is None:
                self.right_child = binaryTree(node)
            else:
                self.right_child.insert(node)

    def __repr__(self):
        return str(self.node)



alist = [10, 8, -4, 71, 18, 93, 21, 30, 15]
tree = binaryTree(2)
for number in alist:
    tree.insert(number)


assert repr(tree.left_child) == "-4"
assert repr(tree.right_child) == "10"
assert repr(tree.right_child.left_child) == "8"
assert repr(tree.right_child.right_child) == "71"
assert repr(tree.right_child.right_child.left_child) == "18"
assert repr(tree.right_child.right_child.left_child.left_child) == "15"



"""

Tree crude representation
            2
     -4                 10
                    8       71
                          18   93
                        15|21
                            30
"""
