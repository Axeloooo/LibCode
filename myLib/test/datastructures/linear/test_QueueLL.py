import pytest
from myLib.src.datastructures.linear.QueueLL import QueueLL
from myLib.src.datastructures.nodes.SNode import SNode


def test_enqueue():
    q = QueueLL()
    q.enqueue(SNode(1))
    q.enqueue(SNode(2))
    q.enqueue(SNode(3))
    assert q.size == 3
    assert q.peek().data == 1


def test_dequeue():
    q = QueueLL()
    q.enqueue(SNode(1))
    q.enqueue(SNode(2))
    q.enqueue(SNode(3))
    dequeued = q.dequeue()
    assert dequeued.data == 1
    assert q.size == 2


def test_peek():
    q = QueueLL()
    q.enqueue(SNode(1))
    q.enqueue(SNode(2))
    assert q.peek().data == 1


def test_is_empty():
    q = QueueLL()
    assert q.is_empty()
    q.enqueue(SNode(1))
    assert not q.is_empty()


def test_search():
    q = QueueLL()
    q.enqueue(SNode(1))
    q.enqueue(SNode(2))
    q.enqueue(SNode(3))
    search_result = q.search(2)
    assert search_result.data == 2
    assert q.size == 3
    search_result = q.search(5)
    assert search_result == -1


def test_clear():
    q = QueueLL()
    q.enqueue(SNode(1))
    q.enqueue(SNode(2))
    q.enqueue(SNode(3))
    q.clear()
    assert q.is_empty()
    assert q.head is None
    assert q.tail is None
