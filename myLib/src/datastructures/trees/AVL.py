# This class is the implementation of the self-balancing AVL tree for integer data members

from myLib.src.datastructures.nodes.TNode import TNode
from myLib.src.datastructures.trees.BST import BST

class AVL(BST):
    def __init__(self, arg = None):
        if isinstance(arg, TNode):
            self.root = None
            if arg.right is not None or arg.left is not None:
                self.create_tree(arg)
        else:
            super().__init__(arg) 
            
    def set_root(self, root):
        if isinstance(root, TNode):
            self.root = None
            if root.right is not None or root.left is not None:
                self.create_tree(root)
        else:
            super().__init__(root)
            
    def get_root(self):
        return self.root
            
    def insert(self, val):
        inserted_node = super().insert(val)
        self.balance_tree(inserted_node)  
        
    def delete(self,val):
        return super().delete(val)
        
    def search(self, val):
        return super().search(val)
        
    def printInOrder(self):
        super().printInOrder()
        
    def printBF(self):
        super().printBF()
        
    def balance_tree(self, node):
        pivot_balance, pivot = self.find_pivot(node)
        if pivot is None:   #case 1
            self.set_balance(self.root)
        else:
            if pivot_balance == 1:
                if node.data < pivot.data:
                    # case = '2'
                    self.set_balance(self.root)
                else:
                    # case = '3'
                    son = pivot.right
                    grandson = son.left
                    if node.data > son.data:                #case 3a
                        self.rotate_left(pivot, son)
                    else:                                   #case 3b
                        if grandson is not None:            
                            self.rotate_right(son, grandson)
                            self.rotate_left(pivot, grandson) 
                        else:
                            self.rotate_right(son, node)
                            self.rotate_left(pivot, node)
                    self.set_balance(self.root)
            else:
                if node.data > pivot.data:
                    # case = '2'
                    self.set_balance(self.root)
                else:
                    # case = '3'
                    son = pivot.left
                    grandson = son.right
                    if node.data < son.data:                 #case 3a
                        self.rotate_right(pivot, son)
                    else:                                    #case 3b
                        if grandson is not None:
                            self.rotate_left(son, grandson)
                            self.rotate_right(pivot, grandson)
                        else:
                            self.rotate_left(son, node)
                            self.rotate_right(pivot, node)
                    self.set_balance(self.root)  
            
    def find_pivot(self, node):
        current = node.parent
        while current is not None:
            if current.balance != 0:
                return current.balance, current
            current = current.parent
        return None, None
                

    def right_height(self, node):                    #recursive function to calculate the height of the right subtree 
        if node is None:
            return -1
        return 1 + self.right_height(node.right)
    
    def left_height(self, node):                    #recursive function to calculate the height of the left subtree
        if node is None:
            return -1
        return 1 + self.left_height(node.left)        
                
    def set_balance(self,node):
        if node is None:
            return
        node.balance = self.right_height(node) - self.left_height(node)
        self.set_balance(node.left)
        self.set_balance(node.right)
        
    def rotate_left(self, pivot, rotator):
        if pivot.parent is not None:
            if pivot.parent.right == pivot:
                pivot.parent.right = rotator
            else:
                pivot.parent.left = rotator
            rotator.parent = pivot.parent
            if rotator.left is not None:
                if pivot.data < rotator.left.data:
                    pivot.right = rotator.left
                    pivot.right.parent = pivot
                else:
                    pivot.left = rotator.right
                    pivot.left.parent = pivot
            else:
                pivot.right = None
            rotator.left = pivot
            pivot.parent = rotator
        else:
            pivot.right = None
            self.root = rotator 
            rotator.parent = None
            if rotator.left is not None:
                pivot.right = rotator.left
                pivot.right.parent = pivot
            rotator.left = pivot
            pivot.parent = rotator
        
    def rotate_right(self, pivot, rotator):
        if pivot.parent is not None:
            if pivot.parent.left == pivot:
                pivot.parent.left = rotator
            else:
                pivot.parent.right = rotator
            rotator.parent = pivot.parent
            if rotator.right is not None:
                if pivot.data > rotator.right.data:
                    pivot.left = rotator.right
                    pivot.left.parent = pivot
                else:
                    pivot.right = rotator.right
                    pivot.right.parent = pivot
            else:
                pivot.left = None
            rotator.right = pivot
            pivot.parent = rotator
        else:
            pivot.left = None
            self.root = rotator
            rotator.parent = None
            if rotator.right is not None:
                pivot.left = rotator.right
                pivot.left.parent = pivot
            rotator.right = pivot
            pivot.parent = rotator
            
    def create_tree(self, node):
        if node is None:
            return
        self.create_tree(node.left)
        self.insert(node.data)
        self.create_tree(node.right)
    
    