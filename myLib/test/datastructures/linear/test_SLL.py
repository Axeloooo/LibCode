import pytest

from myLib.src.datastructures.linear.SLL import SLL
from myLib.src.datastructures.nodes.SNode import SNode


def test_insert_head():
    sll = SLL()
    sll.insert_head(SNode(5))
    assert sll.head.data == 5
    assert sll.tail.data == 5
    assert sll.size == 1
    sll.insert_head(SNode(3))
    assert sll.head.data == 3
    assert sll.tail.data == 5
    assert sll.size == 2


def test_insert_tail():
    sll = SLL()
    sll.insert_tail(SNode(5))
    assert sll.head.data == 5
    assert sll.tail.data == 5
    assert sll.size == 1
    sll.insert_tail(SNode(7))
    assert sll.head.data == 5
    assert sll.tail.data == 7
    assert sll.size == 2


def test_insert():
    sll = SLL()
    with pytest.raises(IndexError):
        sll.insert(SNode(5), -1)
    with pytest.raises(IndexError):
        sll.insert(SNode(5), 1)
    sll.insert(SNode(5), 0)
    assert sll.head.data == 5
    assert sll.tail.data == 5
    assert sll.size == 1
    sll.insert(SNode(3), 0)
    sll.insert(SNode(7), 2)
    assert sll.head.data == 3
    assert sll.tail.data == 7
    assert sll.size == 3


def test_is_sorted():
    sll = SLL()
    sll.insert_tail(SNode(3))
    sll.insert_tail(SNode(5))
    sll.insert_tail(SNode(7))
    assert sll.is_sorted() is True
    sll.insert_head(SNode(9))
    assert sll.is_sorted() is False


def test_sort():
    sll = SLL()
    sll.insert_tail(SNode(7))
    sll.insert_tail(SNode(5))
    sll.insert_tail(SNode(3))
    sll.sort()
    assert sll.is_sorted() is True
    assert sll.head.data == 3
    assert sll.tail.data == 7


def test_sorted_insert():
    sll = SLL()
    sll.sorted_insert(SNode(5))
    sll.sorted_insert(SNode(3))
    sll.sorted_insert(SNode(7))
    assert sll.is_sorted() is True
    assert sll.head.data == 3
    assert sll.tail.data == 7
    assert sll.size == 3


def test_search():
    sll = SLL()
    node1 = SNode(3)
    node2 = SNode(5)
    node3 = SNode(7)
    sll.insert_tail(node1)
    sll.insert_tail(node2)
    sll.insert_tail(node3)
    assert sll.search(node1) == node1
    assert sll.search(node2) == node2
    assert sll.search(node3) == node3
    assert sll.search(SNode(9)) is None


def test_delete_head():
    sll = SLL()
    sll.insert_tail(SNode(3))
    sll.insert_tail(SNode(5))
    sll.insert_tail(SNode(7))
    sll.delete_head()
    assert sll.head.data == 5
    assert sll.tail.data == 7
    assert sll.size == 2


def test_delete_tail():
    sll = SLL()
    sll.insert_tail(SNode(3))
    sll.insert_tail(SNode(5))
    sll.insert_tail(SNode(7))
    sll.delete_tail()
    assert sll.head.data == 3
    assert sll.tail.data == 5
    assert sll.size == 2


def test_delete():
    sll = SLL()
    node1 = SNode(3)
    node2 = SNode(5)
    node3 = SNode(7)
    sll.insert_tail(node1)
    sll.insert_tail(node2)
    sll.insert_tail(node3)
    sll.delete(node2)
    assert sll.head.data == 3
    assert sll.tail.data == 7
    assert sll.size == 2


def test_clear():
    sll = SLL()
    sll.insert_tail(SNode(3))
    sll.insert_tail(SNode(5))
    sll.insert_tail(SNode(7))
    sll.clear()
    assert sll.head is None
    assert sll.tail is None
    assert sll.size == 0


def test_print(capsys):
    sll = SLL()
    sll.insert_tail(SNode(3))
    sll.insert_tail(SNode(5))
    sll.insert_tail(SNode(7))
    sll.print()
    captured = capsys.readouterr()
    assert captured.out == "Inserting tail node: 3\nInserting tail node: 5\nInserting tail node: 7\nList Length: 3\nSorted Status: True\nList Content: 3 -> 5 -> 7 -> "
