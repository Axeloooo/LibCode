import pytest
from myLib.src.datastructures.linear.StackLL import StackLL
from myLib.src.datastructures.nodes.SNode import SNode


def test_push():
    s = StackLL()
    s.push(SNode(1))
    s.push(SNode(2))
    s.push(SNode(3))
    assert s.size == 3
    assert s.peek().data == 3


def test_pop():
    s = StackLL()
    s.push(SNode(1))
    s.push(SNode(2))
    s.push(SNode(3))
    popped = s.pop()
    assert popped.data == 3
    assert s.size == 2


def test_peek():
    s = StackLL()
    s.push(SNode(1))
    s.push(SNode(2))
    assert s.peek().data == 2


def test_is_empty():
    s = StackLL()
    assert s.is_empty()
    s.push(SNode(1))
    assert not s.is_empty()


def test_search():
    stack = StackLL()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    search_result = stack.search(2)
    assert search_result.data == 2
    assert stack.size == 3
    search_result = stack.search(5)
    assert search_result == -1


def test_clear():
    stack = StackLL()
    stack.push(SNode(1))
    stack.push(SNode(2))
    stack.push(SNode(3))
    stack.clear()
    assert stack.is_empty()
    assert stack.head is None
    assert stack.tail is None
