import pytest
from myLib.src.datastructures.linear.CSLL import CSLL
from myLib.src.datastructures.nodes.SNode import SNode


def test_insert_head():
    csll = CSLL()
    csll.insert_head(SNode(2))
    assert csll.head.data == 2
    assert csll.tail.data == 2
    assert csll.size == 1
    csll.insert_head(SNode(1))
    assert csll.head.data == 1
    assert csll.tail.data == 2
    assert csll.size == 2


def test_insert_tail():
    csll = CSLL()
    csll.insert_tail(SNode(1))
    assert csll.head.data == 1
    assert csll.tail.data == 1
    assert csll.size == 1
    csll.insert_tail(SNode(2))
    assert csll.head.data == 1
    assert csll.tail.data == 2
    assert csll.size == 2


def test_insert():
    csll = CSLL()
    csll.insert(SNode(1), 0)
    assert csll.head.data == 1
    assert csll.tail.data == 1
    assert csll.size == 1
    csll.insert(SNode(3), 1)
    assert csll.head.data == 1
    assert csll.tail.data == 3
    assert csll.size == 2
    csll.insert(SNode(2), 1)
    assert csll.head.data == 1
    assert csll.head.next.data == 2
    assert csll.tail.data == 3
    assert csll.size == 3


def test_is_sorted():
    csll = CSLL()
    assert csll.is_sorted()
    csll.insert_tail(SNode(1))
    csll.insert_tail(SNode(2))
    csll.insert_tail(SNode(3))
    assert csll.is_sorted()
    csll.insert_tail(SNode(0))
    assert not csll.is_sorted()


def test_sort():
    csll = CSLL()
    csll.insert_tail(SNode(3))
    csll.insert_tail(SNode(1))
    csll.insert_tail(SNode(2))
    assert not csll.is_sorted()
    csll.sort()
    assert csll.is_sorted()


def test_sorted_insert():
    csll = CSLL()
    csll.sorted_insert(SNode(2))
    assert csll.head.data == 2
    assert csll.tail.data == 2
    assert csll.size == 1
    csll.sorted_insert(SNode(1))
    assert csll.head.data == 1
    assert csll.tail.data == 2
    assert csll.size == 2
    csll.sorted_insert(SNode(3))
    assert csll.head.data == 1
    assert csll.head.next.data == 2
    assert csll.tail.data == 3
    assert csll.size == 3


def test_search():
    csll = CSLL()
    node1 = SNode(1)
    node2 = SNode(2)
    node3 = SNode(3)
    csll.insert_tail(node1)
    csll.insert_tail(node2)
    csll.insert_tail(node3)
    assert csll.search(node1) == node1
    assert csll.search(node2) == node2
    assert csll.search(node3) == node3
    non_existent_node = SNode(4)
    assert csll.search(non_existent_node) is None


def test_delete_head():
    csll = CSLL()
    csll.insert_tail(SNode(1))
    csll.insert_tail(SNode(2))
    csll.insert_tail(SNode(3))
    csll.delete_head()
    assert csll.head.data == 2
    assert csll.tail.data == 3
    assert csll.size == 2


def test_delete_tail():
    csll = CSLL()
    csll.insert_tail(SNode(1))
    csll.insert_tail(SNode(2))
    csll.insert_tail(SNode(3))
    csll.delete_tail()
    assert csll.head.data == 1
    assert csll.tail.data == 2
    assert csll.size == 2


def test_delete():
    csll = CSLL()
    csll.insert_tail(SNode(1))
    csll.insert_tail(SNode(2))
    csll.insert_tail(SNode(3))
    csll.delete(csll.head.next)
    assert csll.head.data == 1
    assert csll.tail.data == 3
    assert csll.size == 2


def test_clear():
    csll = CSLL()
    csll.insert_tail(SNode(1))
    csll.insert_tail(SNode(2))
    csll.insert_tail(SNode(3))
    csll.clear()
    assert csll.head is None
    assert csll.tail is None
    assert csll.size == 0
