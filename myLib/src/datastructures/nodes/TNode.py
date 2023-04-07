# This is a general tree node class that has requirements for both BST and AVL trees

class TNode:
    def __init__(self, data=None, balance=0, parent=None, left=None, right=None):
        self.data = data
        self.balance = balance
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def print_node(self):
        print(f"Data: {self.data}, Balance: {self.balance}")

