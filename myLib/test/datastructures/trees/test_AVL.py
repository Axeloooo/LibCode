import pytest

from myLib.src.datastructures.trees.BST import BST
from myLib.src.datastructures.nodes.TNode import TNode
from myLib.src.datastructures.trees.AVL import AVL

def test_constructor():
    ##testing whether constructor that takes a node as an argument can create a balanced tree from the passed in tree
    
    tnode = TNode(9)
    bst = BST(tnode)
    bst.insert(7)
    bst.insert(8)
    bst.insert(5)
    bst.insert(17)
    bst.insert(12)
    bst.insert(10)
    bst.insert(14)
    bst.insert(19)
    bst.insert(21)

    avl = AVL(tnode)
    string_output = "9\n7 17\n5 8 12 19\n10 14 21"
    
    assert avl.printBF() == print(string_output)
    
def test_set_root():
    avl = AVL()
    avl.set_root(3)
    assert avl.root.data == 3
    
    tnode = TNode(5)
    tnode.set_right(7)
    tnode.get_right().set_right(8)
    
    avl.set_root(tnode)
    assert avl.root.data == 7
    assert avl.root.get_right().data == 8
    assert avl.root.get_left().data == 5
    
def test_get_root():
    avl = AVL()
    avl.set_root(3)
    assert avl.get_root().data == 3
    
    tnode = TNode(5)
    tnode.set_right(7)
    tnode.get_right().set_right(8)
    
    avl.set_root(tnode)
    assert avl.get_root().data == 7
    assert avl.get_root().get_right().data == 8
    assert avl.get_root().get_left().data == 5
    
def test_insert_with_integer():
    
    avl = AVL(30)
    avl.insert(40)
    avl.insert(60)
    avl.insert(70)
    avl.insert(80)
    avl.insert(90)
    avl.insert(95)
    avl.insert(5)
    avl.insert(6)
    avl.insert(12)

    string_output = "70\n30 90\n6 40 80 95\n5 12 60"
    assert avl.printBF() == print(string_output)
    
def test_insert_with_node():
    avl = AVL(TNode(30))
    avl.insert(TNode(40))
    avl.insert(TNode(60))
    avl.insert(TNode(70))
    avl.insert(TNode(80))
    avl.insert(TNode(90))
    avl.insert(TNode(95))
    avl.insert(TNode(5))
    avl.insert(TNode(6))
    avl.insert(TNode(12))

    string_output = "70\n30 90\n6 40 80 95\n5 12 60"
    assert avl.printBF() == print(string_output)

def test_search():
    avl = AVL(30)
    avl.insert(40)
    avl.insert(60)
    avl.insert(70)
    avl.insert(80)
    avl.insert(90)
    avl.insert(95)
    avl.insert(5)
    avl.insert(6)
    avl.insert(12)
    
    assert isinstance(avl.search(40), TNode) == True
    assert avl.search(40).data == 40
    assert avl.search(7) == None

def test_delete():

    avl = AVL(2)
    avl.insert(5)
    avl.insert(7)
    avl.insert(10)
    avl.insert(12)
    avl.insert(17)
    avl.insert(20)

    assert avl.delete(4) == "Value is not in the tree"

    avl.delete(17)
    assert avl.search(17) == None
    
def test_printInOrder():
    
    avl = AVL(10)
    avl.insert(5)
    avl.insert(7)
    avl.insert(2)
    avl.insert(20)
    avl.insert(12)
    avl.insert(17)

    string = "2\n5\n7\n10\n12\n17\n20"
    
    assert avl.printInOrder() == print(string)
    
def test_printBF():
    avl = AVL(10)
    avl.insert(5)
    avl.insert(7)
    avl.insert(2)
    avl.insert(20)
    avl.insert(12)
    avl.insert(17)
    
    string = "7\n5 12\n2 10 20\n17"  
    
    assert avl.printBF() == print(string)