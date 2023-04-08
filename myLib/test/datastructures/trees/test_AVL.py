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
    
def test_insert():
    
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
    
    


    
    