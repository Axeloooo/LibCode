# This is a doubly Linked List data structure

from myLib.src.datastructures.nodes.DNode import DNode
from myLib.src.datastructures.linear.SLL import SLL


class DLL(SLL):
    def __init__(self, node=None):
        super().__init__(node)
        if node:
            node.prev = None
            self.tail.prev = None

    def insert_head(self, node):
        super().insert_head(node)
        if self.size == 2:
            self.head.next.prev = self.head

    def insert_tail(self, node):
        if self.tail is None:
            super().insert_tail(node)
        else:
            print("Inserting tail node:", node.data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def insert(self, node, position):
        if position == 0:
            self.insert_head(node)
        elif position == self.size:
            self.insert_tail(node)
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            print("Inserting node:", node.data)
            node.next = current.next
            node.prev = current
            current.next.prev = node
            current.next = node
            self.size += 1

    def sorted_insert(self, node):
        super().sorted_insert(node)

    def delete_head(self):
        super().delete_head()
        if self.head:
            self.head.prev = None

    def delete_tail(self):
        if self.head:
            if self.head == self.tail:
                print("Deleting tail node:", self.tail.data)
                self.head = None
                self.tail = None
            else:
                print("Deleting tail node:", self.tail.data)
                self.tail = self.tail.prev
                self.tail.next = None
            self.size -= 1

    def delete(self, node):
        if self.head == node:
            self.delete_head()
        elif self.tail == node:
            self.delete_tail()
        else:
            current = self.head
            while current:
                if current == node:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    return
                current = current.next
