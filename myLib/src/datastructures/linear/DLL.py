# This is a doubly Linked List data structure

from myLib.datastructures.nodes.DNode import DNode


class DLL():
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0 if head is None else 1

    def insert_head(self, DNode):
        pass
