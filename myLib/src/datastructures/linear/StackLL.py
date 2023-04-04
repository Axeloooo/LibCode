# This is a Stack based on Singly Linked List data structure

from myLib.src.datastructures.linear.SLL import SLL


class StackLL(SLL):
    def init(self, node=None):
        super().init(node)

    def insert_tail(self, node):
        pass

    def insert(self, node, position):
        pass

    def is_sorted(self):
        pass

    def sort(self):
        pass

    def sorted_insert(self, node):
        pass

    def delete_tail(self):
        pass

    def delete(self, node):
        pass

    def push(self, node):
        super().insert_head(node)

    def pop(self):
        if self.head:
            popped_node = self.head
            super().delete_head()
            return popped_node
        else:
            return None

    def peek(self):
        return self.head

    def is_empty(self):
        return self.size == 0

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return -1

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print(self):
        print(f"Stack Size: {self.size}")
        print("Stack Content:", end=" ")
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
