import pytest

from myLib.src.datastructures.trees.BST import BST
from myLib.src.datastructures.nodes.TNode import TNode

def test_constructor():
    bst1 = BST(TNode(10))
    assert bst1.root.data == 10
    
    bst2 = BST(5)
    assert bst2.root.data == 5
    
    bst3 = BST()
    assert bst3.root is None
    
def test_insert_with_integer():
    bst = BST()
    bst.insert(10)
    assert bst.root.data == 10
    bst.insert(5)
    bst.insert(17)
    assert bst.root.left.data == 5
    assert bst.root.right.data == 17
    
def test_insert_with_node():
    bst = BST()
    bst.insert(TNode(8))
    assert bst.root.data == 8
    bst.insert(TNode(4))
    bst.insert(TNode(12))
    assert bst.root.left.data == 4
    assert bst.root.right.data == 12
    
def test_search():
    bst = BST(4)
    bst.insert(2)
    bst.insert(TNode(5))
    bst.insert(TNode(3))
    bst.insert(10)
    
    assert isinstance(bst.search(2), TNode) == True
    assert bst.search(2).data == 2
    assert bst.search(7) == None

def test_delete():
    bst = BST(10)
    bst.insert(5)
    bst.insert(17)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    
    assert bst.delete(21) == "Value is not in the tree"
    
    bst.delete(10)
    assert bst.search(10) == None
    assert bst.root.data == 12
    bst.delete(17)
    assert bst.root.right.data == 20

def test_printInOrder():
    bst = BST(10)
    bst.insert(5)
    bst.insert(17)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    
    string = "2\n5\n7\n10\n12\n17\n20"
    
    assert bst.printInOrder() == print(string)
    
def test_printBF():
    bst = BST(10)
    bst.insert(5)
    bst.insert(17)
    bst.insert(2)
    bst.insert(7)
    bst.insert(12)
    bst.insert(20)
    
    string = "10\n5 17\n2 7 12 20"
    
    assert bst.printBF() == print(string)
    
    



