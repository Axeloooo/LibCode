# This class is the implementation of the Binary Search Tree (BST) for integer data

from myLib.src.datastructures.nodes.TNode import TNode

class BST():
    def __init__(self, arg = None):
        self.root = None
        if isinstance(arg, TNode):
            self.root = arg
        elif isinstance(arg, int):
            self.root = TNode(arg)
            
    def insert(self, arg):
        current = self.root
        parent = None
        if isinstance(arg, TNode):      ##if arg is TNode
            newnode = arg
            data = arg.data
        else:                           ##if arg is int
            newnode = TNode(arg)
            data = arg
            
        while current is not None:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right
        
        newnode.parent = parent
        if self.root is None:
            self.root = newnode
        elif data < parent.data:
            parent.left = newnode
        else:
            parent.right = newnode
        
        return newnode

            
    def delete(self, val):
        node_to_delete = self.search(val)
        if node_to_delete is None:
            return "Value is not in the tree"
        elif node_to_delete.left == None and node_to_delete.right == None:      ##if node_to_delete is a leaf
            if node_to_delete == self.root:
                self.root = None
            else:
                if node_to_delete.parent.right == node_to_delete:
                    node_to_delete.parent.right = None
                else:
                    node_to_delete.parent.left = None
        elif node_to_delete.left is not None and node_to_delete.right is not None:  
            successor = node_to_delete.right
            while successor.left is not None:
                successor = successor.left
            self.delete(successor.data)
            node_to_delete.data = successor.data
        else:                       
            if node_to_delete == self.root:
                if node_to_delete.right is None:
                    self.root = node_to_delete.left
                else:
                    self.root = node_to_delete.right
            else:
                if node_to_delete.parent.left == node_to_delete:
                    if node_to_delete.left is None:
                        node_to_delete.parent.left = node_to_delete.right
                    else:
                        node_to_delete.parent.left = node_to_delete.left
                else:
                    if node_to_delete.left is None:
                        node_to_delete.parent.right = node_to_delete.right
                    else:
                        node_to_delete.parent.right = node_to_delete.left      
    
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def printInOrder(self):
        def inorderTraversal(node):
            if node is not None:
                inorderTraversal(node.left)
                print(node.data)
                inorderTraversal(node.right)
        inorderTraversal(self.root)
        
        
    def printBF(self):
        if self.root is None:
            return
        
        queue = []
        queue.append(self.root)
        current_level_count = 1
        next_level_count = 0
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.data, end=' ')
            current_level_count -= 1
            if current.left is not None:
                queue.append(current.left)
                next_level_count += 1
            if current.right is not None:
                queue.append(current.right)
                next_level_count += 1
            if current_level_count == 0:
                print('')
                current_level_count = next_level_count
                next_level_count = 0


            
        
        