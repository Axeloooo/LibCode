# This is a Singly Linked List Data structure

from myLib.src.datastructures.nodes.SNode import SNode


class SLL():
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.size = 0 if head is None else 1

    def insert_head(self, node):
        if self.head is None:
            print("Inserting head node:", node.data)
            self.head = node
            self.tail = node
        else:
            print("Inserting head node:", node.data)
            node.next = self.head
            self.head = node
        self.size += 1

    def insert_tail(self, node):
        if self.tail is None:
            print("Inserting tail node:", node.data)
            self.head = node
            self.tail = node
        else:
            print("Inserting tail node:", node.data)
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insert(self, node, position):
        if position < 0 or position > self.size:
            raise IndexError("Invalid position")
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
            current.next = node
            self.size += 1

    def is_sorted(self):
        if self.head == None:
            return True
        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def sort(self):
        if not self.is_sorted():
            sorted_list = SLL()
            current = self.head
            while current:
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
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1

    def search(self, node):
        current = self.head
        while current:
            if current == node:
                return current
            current = current.next
        return None

    def delete_head(self):
        if self.head:
            print("Deleting head node:", self.head.data)
            self.head = self.head.next
            self.size -= 1
            if self.size == 0:
                self.tail = None

    def delete_tail(self):
        if self.head:
            if self.head == self.tail:
                print("Deleting tail node:", self.tail.data)
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                print("Deleting tail node:", current.next.data)
                current.next = None
                self.tail = current
            self.size -= 1

    def delete(self, node):
        if self.head == node:
            self.delete_head()
        elif self.tail == node:
            self.delete_tail()
        else:
            current = self.head
            while current.next and current.next != node:
                current = current.next
            if current.next:
                print("Deleting node:", current.next.data)
                current.next = current.next.next
                self.size -= 1

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print(self):
        print(f"List Length: {self.size}")
        print("Sorted Status:", self.is_sorted())
        print("List Content:", end=" ")
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
