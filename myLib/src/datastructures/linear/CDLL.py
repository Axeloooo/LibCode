# This is a Circular Doubly Linked List data structure

from myLib.src.datastructures.linear.DLL import DLL
from myLib.src.datastructures.nodes.DNode import DNode


class CDLL(DLL):
    def __init__(self, node=None):
        super().__init__(node)
        if node:
            self.head.prev = self.tail
            self.tail.next = self.head

    def insert_head(self, node):
        super().insert_head(node)
        self.head.prev = self.tail
        self.tail.next = self.head

    def insert_tail(self, node):
        super().insert_tail(node)
        self.tail.next = self.head
        self.head.prev = self.tail

    def is_sorted(self):
        if self.size <= 1:
            return True
        current = self.head
        for _ in range(self.size - 1):
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        if self.size > 1:
            current = self.head
            for _ in range(self.size):
                swap = False
                inner_current = self.head
                for _ in range(self.size - 1):
                    if inner_current.data > inner_current.next.data:
                        inner_current.data, inner_current.next.data = inner_current.next.data, inner_current.data
                        swap = True
                    inner_current = inner_current.next
                if not swap:
                    break

    def sorted_insert(self, node):
        if self.head is None or node.data <= self.head.data:
            self.insert_head(node)
        elif node.data >= self.tail.data:
            self.insert_tail(node)
        else:
            current = self.head
            for _ in range(self.size - 1):
                if current.next.data >= node.data:
                    break
                current = current.next
            node.next = current.next
            node.prev = current
            current.next.prev = node
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
                self.head, self.tail = None, None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            self.size -= 1

    def delete_tail(self):
        if self.tail:
            if self.head == self.tail:
                self.head, self.tail = None, None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
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
            for _ in range(self.size):
                if current == node:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    return
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
