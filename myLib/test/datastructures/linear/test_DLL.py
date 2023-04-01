import pytest
from myLib.src.datastructures.nodes.SNode import SNode
from myLib.src.datastructures.nodes.DNode import DNode
from myLib.src.datastructures.linear.SLL import SLL
from myLib.src.datastructures.linear.DLL import DLL


def test_insert_head():
    dll = DLL()
    dll.insert_head(DNode(1))
    assert dll.head.data == 1
    assert dll.tail.data == 1
    dll.insert_head(DNode(0))
    assert dll.head.data == 0
    assert dll.tail.data == 1


def test_insert_tail():
    dll = DLL()
    dll.insert_tail(DNode(1))
    assert dll.head.data == 1
    assert dll.tail.data == 1
    dll.insert_tail(DNode(2))
    assert dll.head.data == 1
    assert dll.tail.data == 2


def test_insert():
    dll = DLL()
    dll.insert(DNode(1), 0)
    dll.insert(DNode(2), 1)
    dll.insert(DNode(0), 0)
    dll.insert(DNode(3), 3)
    dll.insert(DNode(4), 4)
    assert [node.data for node in dll] == [0, 1, 2, 3, 4]


def test_is_sorted():
    dll = DLL()
    dll.insert_head(DNode(1))
    dll.insert_head(DNode(0))
    assert dll.is_sorted() == True


def test_sort():
    dll = DLL()
    dll.insert_head(DNode(2))
    dll.insert_head(DNode(1))
    dll.insert_head(DNode(0))
    dll.insert_tail(DNode(4))
    dll.insert(DNode(3), 3)
    dll.sort()
    assert dll.is_sorted() == True


def test_sorted_insert():
    dll = DLL()
    dll.insert_head(DNode(2))
    dll.insert_head(DNode(1))
    dll.insert_head(DNode(0))
    dll.sorted_insert(DNode(3))
    assert dll.is_sorted() == True


def test_search():
    dll = DLL()
    node1 = DNode(1)
    node2 = DNode(2)
    dll.insert_head(node1)
    dll.insert_tail(node2)
    assert dll.search(node1) == node1
    assert dll.search(node2) == node2
    assert dll.search(DNode(3)) == None


def test_delete_head():
    dll = DLL()
    dll.insert_head(DNode(1))
    dll.insert_head(DNode(0))
    dll.delete_head()
    assert dll.head.data == 1


def test_delete_tail():
    dll = DLL()
    dll.insert_head(DNode(1))
    dll.insert_head(DNode(0))
    dll.delete_tail()
    assert dll.tail.data == 0


def test_delete():
    dll = DLL()
    dll.insert_head(DNode(2))
    dll.insert_head(DNode(1))
    dll.insert_head(DNode(0))
    dll.delete(DNode(1))
    assert [node.data for node in dll] == [0, 2]


def test_clear():
    dll = DLL()
    dll.insert_head(DNode(1))
    dll.insert_head(DNode(0))
    dll.clear()
    assert dll.head == None
    assert dll.tail == None


def test_print(capsys):
    dll = DLL()
    dll.insert_head(DNode(1))
    dll.insert_head(DNode(0))
    dll.insert_tail(DNode(2))
    dll.print()

    captured = capsys.readouterr()
    assert "List Length: 3" in captured.out
    assert "Sorted Status: True" in captured.out
    assert "List Content: 0 -> 1 -> 2 -> " in captured.out
