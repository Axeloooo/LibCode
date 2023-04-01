# This is a Node for a Doubly Linked List Data structure

class DNode(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
