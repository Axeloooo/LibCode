# This is a Circular Singly Linked List data structure

from myLib.src.datastructures.linear.SLL import SLL
from myLib.src.datastructures.nodes.SNode import SNode


class CSLL(SLL):
    def init(self, node=None):
        super().init(node)
        if node:
            node.next = node

    def insert_head(self, node):
        if self.head is None:
            node.next = node
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        self.size += 1

    def insert_tail(self, node):
        if self.tail is None:
            node.next = node
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.tail = node
        self.size += 1

    def is_sorted(self):
        if self.head is None or self.size == 1:
            return True
        current = self.head
        for _ in range(self.size - 1):
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        if not self.is_sorted():
            sorted_list = CSLL()
            current = self.head
            for _ in range(self.size):
                sorted_list.sorted_insert(SNode(current.data))
                current = current.next
            self.head = sorted_list.head
            self.tail = sorted_list.tail

    def sorted_insert(self, node):
        if not self.is_sorted():
            self.sort()
        if self.head is None or node.data <= self.head.data:
            self.insert_head(node)
        elif node.data >= self.tail.data:
            self.insert_tail(node)
        else:
            current = self.head
            for _ in range(self.size - 1):
                if current.next.data > node.data:
                    break
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def search(self, node):
        current = self.head
        for _ in range(self.size):
            if current == node:
                return current
            current = current.next
        return None

    def delete_head(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            self.size -= 1

    def delete_tail(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = self.head
                self.tail = current
            self.size -= 1

    def delete(self, node):
        if self.head is None:
            return
        if self.head == node:
            self.delete_head()
        elif self.tail == node:
            self.delete_tail()
        else:
            current = self.head
            for _ in range(self.size - 1):
                if current.next == node:
                    current.next = current.next.next
                    self.size -= 1
                    break
                current = current.next

    def print(self):
        print(f"List Length: {self.size}")
        print("Sorted Status:", self.is_sorted())
        print("List Content:", end=" ")
        current = self.head
        for _ in range(self.size):
            print(current.data, end=" -> ")
            current = current.next
        print("Loop back to head:", current.data)
