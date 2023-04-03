import pytest
from myLib.src.datastructures.linear.CDLL import CDLL
from myLib.src.datastructures.nodes.DNode import DNode


def test_insert_head():
    cdll = CDLL()
    cdll.insert_head(DNode(2))
    assert cdll.head.data == 2
    assert cdll.tail.data == 2
    assert cdll.head.next == cdll.tail
    assert cdll.tail.next == cdll.head
    cdll.insert_head(DNode(1))
    assert cdll.head.data == 1
    assert cdll.tail.data == 2
    assert cdll.head.next == cdll.tail
    assert cdll.tail.next == cdll.head


def test_insert_tail():
    cdll = CDLL()
    cdll.insert_tail(DNode(1))
    assert cdll.head.data == 1
    assert cdll.tail.data == 1
    assert cdll.head.next == cdll.tail
    assert cdll.tail.next == cdll.head
    cdll.insert_tail(DNode(2))
    assert cdll.head.data == 1
    assert cdll.tail.data == 2
    assert cdll.head.next == cdll.tail
    assert cdll.tail.next == cdll.head


def test_insert():
    cdll = CDLL()
    cdll.insert(DNode(2), 0)
    cdll.insert(DNode(1), 0)
    cdll.insert(DNode(4), 2)
    cdll.insert(DNode(3), 2)
    assert cdll.head.data == 1
    assert cdll.head.next.data == 2
    assert cdll.head.next.next.data == 3
    assert cdll.tail.data == 4
    assert cdll.head.prev == cdll.tail
    assert cdll.tail.next == cdll.head


def test_is_sorted():
    cdll = CDLL()
    cdll.insert_head(DNode(1))
    cdll.insert_head(DNode(2))
    cdll.insert_head(DNode(3))
    assert not cdll.is_sorted()
    cdll.sort()
    assert cdll.is_sorted()
    cdll.delete_head()
    assert cdll.is_sorted()


def test_sort():
    cdll = CDLL()
    cdll.insert_head(DNode(3))
    cdll.insert_head(DNode(1))
    cdll.insert_head


def test_sorted_insert():
    cdll = CDLL()
    cdll.sorted_insert(DNode(3))
    cdll.sorted_insert(DNode(1))
    cdll.sorted_insert(DNode(2))
    cdll.sorted_insert(DNode(5))
    cdll.sorted_insert(DNode(4))
    assert cdll.head.data == 1
    assert cdll.head.next.data == 2
    assert cdll.head.next.next.data == 3
    assert cdll.head.next.next.next.data == 4
    assert cdll.tail.data == 5
    assert cdll.head.prev == cdll.tail
    assert cdll.tail.next == cdll.head


def test_search():
    cdll = CDLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    cdll.insert_head(node1)
    cdll.insert_tail(node2)
    cdll.insert_tail(node3)
    assert cdll.search(node1) == node1
    assert cdll.search(node2) == node2
    assert cdll.search(node3) == node3
    assert cdll.search(node4) is None


def test_delete_head():
    cdll = CDLL()
    cdll.insert_head(DNode(2))
    cdll.insert_head(DNode(1))
    cdll.delete_head()
    assert cdll.head.data == 2
    assert cdll.tail.data == 2
    assert cdll.head.next == cdll.tail
    assert cdll.tail.next == cdll.head


def test_delete_tail():
    cdll = CDLL()
    cdll.insert_head(DNode(2))
    cdll.insert_head(DNode(1))
    cdll.delete_tail()
    assert cdll.head.data == 1
    assert cdll.tail.data == 1
    assert cdll.head.next == cdll.tail
    assert cdll.tail.next == cdll.head


def test_delete():
    cdll = CDLL()
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node4 = DNode(4)
    cdll.insert_head(node1)
    cdll.insert_tail(node2)
    cdll.insert_tail(node3)
    cdll.insert_tail(node4)
    cdll.delete(node2)
    assert cdll.head.data == 1
    assert cdll.head.next.data == 3
    assert cdll.head.next.next.data == 4
    assert cdll.tail.data == 4
    assert cdll.head.prev == cdll.tail
    assert cdll.tail.next == cdll.head
    assert cdll.size == 3


def test_clear():
    cdll = CDLL()
    cdll.insert_head(DNode(1))
    cdll.insert_tail(DNode(2))
    cdll.insert_tail(DNode(3))
    cdll.clear()
    assert cdll.head is None
    assert cdll.tail is None
    assert cdll.size == 0
