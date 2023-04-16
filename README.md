# LibCode

![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white) ![](https://img.shields.io/badge/Pytest-0A9EDC.svg?style=for-the-badge&logo=Pytest&logoColor=white) ![](https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white) ![](https://img.shields.io/badge/Git-F05032.svg?style=for-the-badge&logo=Git&logoColor=white) ![](https://img.shields.io/badge/macOS-000000.svg?style=for-the-badge&logo=macOS&logoColor=white)

### PyPi Package URL

```bash
https://pypi.org/project/LibCode/1.1.0/
```

### Collaborators

- Axel Sanchez
- Mariia Podgaietska

# Get Started

## Introduction

This is a library that contains a set of data structures and algorithms that are used in the development of software. The library is written in Python and contains the following data structures:

- Stack
- Queue
- Singly Linked List
- Doubly Linked List
- Circular Singly Linked List
- Circular Doubly Linked List
- Binary Search Tree
- AVL Tree

## Installation

```bash
pip install LibCode
```

## Overview

The library contains the following modules:

- `myLib.src.data_structures.linear`
- `myLib.src.data_structures.nodes`
- `myLib.src.data_structures.trees`
- `myLib.test.data_structures.linear`
- `myLib.test.data_structures.trees`

The myLib.src.data_structures.linear module contains the following classes:

- StackLL
- QueueLL
- SLL
- DLL
- CLL
- CDLL

The myLib.src.data_structures.nodes module contains the following classes:

- SNode
- DNode
- TNode

The myLib.src.data_structures.trees module contains the following classes:

- BST
- AVL

The myLib.test.data_structures.linear module contains the following classes:

- test_StackLL
- test_QueueLL
- test_SLL
- test_DLL
- test_CLL
- test_CDLL

The myLib.test.data_structures.trees module contains the following classes:

- test_BST
- test_AVL

## Testing

To run the tests, first, install the pytest package:

```bash
pip install pytest
```

Then, run the following command:

```bash
python -m pytest -v
```

# Documentation

## Single Node

The SNode class is a simple implementation of a node for a Singly Linked List data structure. Each node in a Singly Linked List contains two attributes: the data it holds and a reference to the next node in the list.

```python
from myLib import SNode
```

Here's a brief explanation of the SNode class attributes and methods:

- Attributes:

1. data: The data the node holds. It can be any data type (e.g., integer, string, object).
2. next: A reference to the next node in the Singly Linked List. The value is None for the last node in the list.

- Methods:

1. **init**(self, data=None): Initializes a new instance of the SNode class with the specified data. By default, the data is set to None.

To create and manipulate nodes using the SNode class, follow these steps:

1. Create an instance of the SNode class and set the data:

```python
node1 = SNode(1)
```

Create another instance and set the data:

```python
node2 = SNode(2)
```

Link the first node to the second node by setting the next attribute of the first node:

```python
node1.next = node2
```

Now you have two nodes in a Singly Linked List. You can continue adding more nodes and linking them together using their next attribute.

For more advanced operations on a Singly Linked List, such as inserting, deleting, or searching nodes, use the SLL class provided earlier in this conversation.

## Double Node

The DNode class is an implementation of a node for a Doubly Linked List data structure. Each node in a Doubly Linked List contains three attributes: the data it holds, a reference to the next node in the list, and a reference to the previous node in the list.

```python
from myLib import DNode
```

Here's a brief explanation of the DNode class attributes and methods:

- Attributes:

1. data: The data the node holds. It can be any data type (e.g., integer, string, object).
2. next: A reference to the next node in the Doubly Linked List. The value is None for the last node in the list.
3. prev: A reference to the previous node in the Doubly Linked List. The value is None for the first node in the list.

- Methods:

1. **init**(self, data=None): Initializes a new instance of the DNode class with the specified data. By default, the data is set to None.

To create and manipulate nodes using the DNode class, follow these steps:

1. Create an instance of the DNode class and set the data:

```python
node1 = DNode(1)
```

2. Create another instance and set the data:

```python
node2 = DNode(2)
```

3. Link the first node to the second node by setting the next attribute of the first node and the prev attribute of the second node:

```python
node1.next = node2
node2.prev = node1
```

Now you have two nodes in a Doubly Linked List. You can continue adding more nodes and linking them together using their next and prev attributes.

For more advanced operations on a Doubly Linked List, such as inserting, deleting, or searching nodes, use the DLL class provided earlier in this conversation.

## Tree Node

This TNode class represents a general tree node that can be used for both Binary Search Trees (BST) and AVL trees.

```python
from myLib import TNode
```

The class has several attributes and methods designed to work with tree-based data structures:

- Attributes:

1. data: The data the node holds. It can be any data type (e.g., integer, string, object).
2. balance: The balance factor of the node, used for AVL trees to determine if the tree is balanced or requires rotation.
3. parent: A reference to the parent node.
4. left: A reference to the left child node.
5. right: A reference to the right child node.

- Methods:

1. **init**(self, data=None, balance=0, parent=None, left=None, right=None): Initializes a new instance of the TNode class with the specified data, balance factor, parent, left child, and right child. By default, all values are set to None, and the balance factor is set to 0.
2. Setter methods: set_data, set_balance, set_parent, set_left, and set_right are used to set the corresponding attributes of a TNode instance.
3. Getter methods: get_data, get_balance, get_parent, get_left, and get_right are used to retrieve the corresponding attributes of a TNode instance.
4. **str**(self): Returns the string representation of the node's data.
5. print_node(self): Prints the node's data, balance factor, parent, left child, and right child.

To create and manipulate nodes using the TNode class, follow these steps:

1. Create an instance of the TNode class and set the data:

```python
node1 = TNode(1)
```

2. Create another instance and set the data:

```python
node2 = TNode(2)
```

Set the parent, left child, and right child of the nodes using the setter methods:

```python
node1.set_right(node2)
node2.set_parent(node1)
```

Now you have two nodes in a tree structure. You can continue adding more nodes and linking them together using their parent, left, and right attributes.

For more advanced operations on BST or AVL trees, such as inserting, deleting, or searching nodes, you would need to create a tree class that utilizes the TNode class to perform those operations.

## Singly Linked List

The SLL class is an implementation of a singly linked list data structure. It provides methods for creating and manipulating singly linked lists. In a singly linked list, each node contains a reference to the next node, except for the last node, which has a reference to None.

```python
from myLib import SLL
from myLib import SNode
```

Here's a brief explanation of the methods provided by the SLL class:

1. **init**(self, node=None): Initializes a new singly linked list. You can pass an optional node to set as the head and tail of the list.
2. insert_head(self, node): Inserts a new node at the head of the list.
3. insert_tail(self, node): Inserts a new node at the tail of the list.
4. insert(self, node, position): Inserts a new node at the specified position in the list.
5. is_sorted(self): Checks if the list is sorted in ascending order.
6. sort(self): Sorts the list in ascending order.
7. sorted_insert(self, node): Inserts a new node into the list while maintaining the sorted order.
8. search(self, node): Searches for a node in the list and returns it if found, otherwise returns None.
9. delete_head(self): Removes the head node from the list.
10. delete_tail(self): Removes the tail node from the list.
11. delete(self, node): Removes the specified node from the list.
12. clear(self): Removes all nodes from the list, resetting its size to 0.
13. print(self): Prints the list's length, sorted status, and list content.

To use the SLL class, first, create an instance of the class:

```python
slist = SLL()
```

Then, create nodes and use the provided methods to manipulate the list:

```python
node1 = SNode(1)
node2 = SNode(2)
node3 = SNode(3)

slist.insert_head(node1)
slist.insert_tail(node2)
slist.sorted_insert(node3)

slist.print()
```

This will create a singly linked list with three nodes and print its contents.

You can also use other methods to search, delete, and manipulate the list as needed.

## Doubly Linked List

The DLL (Doubly Linked List) class is an implementation of a doubly linked list data structure. It inherits from the SLL (Singly Linked List) class and extends the functionality to support doubly linked nodes, with each node having a reference to both the next node and the previous node.

```python
from myLib import DLL
from myLib import DNode
```

Here's a brief explanation of the methods provided by the DLL class:

1. **init**(self, node=None): Initializes a new doubly linked list. You can pass an optional node to set as the head and tail of the list.
2. insert_head(self, node): Inserts a new node at the head of the doubly linked list.
3. insert_tail(self, node): Inserts a new node at the tail of the doubly linked list.
4. insert(self, node, position): Inserts a new node at the specified position in the doubly linked list.
5. is_sorted(self): Checks if the doubly linked list is sorted in ascending order.
6. sort(self): Sorts the doubly linked list in ascending order.
7. sorted_insert(self, node): Inserts a new node in the sorted doubly linked list while maintaining its sorted order.
8. search(self, node): Searches for a node in the doubly linked list and returns it if found, otherwise returns None.
9. delete_head(self): Removes the head node from the doubly linked list.
10. delete_tail(self): Removes the tail node from the doubly linked list.
11. delete(self, node): Removes the specified node from the doubly linked list.
12. clear(self): Removes all nodes from the doubly linked list, resetting its size to 0.
13. print(self): Prints the doubly linked list's length, sorted status, and list content.

To use the DLL class, first, create an instance of the class:

```python
dlist = DLL()
```

Then, create nodes and use the provided methods to manipulate the doubly linked list:

```python
node1 = DNode(1)
node2 = DNode(2)
node3 = DNode(3)

doubly_linked_list.insert_head(node1)
doubly_linked_list.insert_tail(node2)
doubly_linked_list.insert(node3, 2)

doubly_linked_list.print()
```

This will create a doubly linked list with three nodes and print its contents.

You can also use other methods to search, delete nodes, and manipulate the doubly linked list as needed.

## Stack

The StackLL class is an implementation of a stack data structure based on a singly linked list. It inherits from the SLL (Singly Linked List) class and disables some of the methods not needed for a stack, such as insert_tail, insert, is_sorted, sort, sorted_insert, delete_tail, and delete.

```python
from myLib import StackLL
from myLib import SNode
```

Here's a brief explanation of the methods provided by the StackLL class:

1. **init**(self, node=None): Initializes a new stack based on a singly linked list. You can pass an optional node to set as the head and tail of the list.
2. push(self, node): Inserts a new node at the top of the stack.
3. pop(self): Removes and returns the top node from the stack. If the stack is empty, it returns None.
4. peek(self): Returns the top node of the stack without removing it.
5. is_empty(self): Checks if the stack is empty. Returns True if the stack is empty, and False otherwise.
6. search(self, data): Searches for a node with the specified data in the stack and returns it if found, otherwise returns -1.
7. clear(self): Removes all nodes from the stack, resetting its size to 0.
8. print(self): Prints the stack's size and content.

To use the StackLL class, first, create an instance of the class:

```python
stack = StackLL()
```

Then, create nodes and use the provided methods to manipulate the stack:

```python
node1 = SNode(1)
node2 = SNode(2)
node3 = SNode(3)

stack.push(node1)
stack.push(node2)
stack.push(node3)

stack.print()
```

This will create a stack with three nodes and print its contents.

You can also use other methods to search, pop, and manipulate the stack as needed.

## Queue

The QueueLL class is an implementation of a queue data structure based on a singly linked list. It inherits from the SLL (Singly Linked List) class and disables some of the methods not needed for a queue, such as insert_head, insert, is_sorted, sort, sorted_insert, delete_head, delete_tail, and delete.

```python
from myLib import QueueLL
from myLib import SNode
```

Here's a brief explanation of the methods provided by the QueueLL class:

1. **init**(self, node=None): Initializes a new queue based on a singly linked list. You can pass an optional node to set as the head and tail of the list.
2. enqueue(self, node): Inserts a new node at the rear (tail) of the queue.
3. dequeue(self): Removes and returns the front (head) node from the queue. If the queue is empty, it returns None.
4. peek(self): Returns the front (head) node of the queue without removing it.
5. is_empty(self): Checks if the queue is empty. Returns True if the queue is empty, and False otherwise.
6. search(self, data): Searches for a node with the specified data in the queue and returns it if found, otherwise returns -1.
7. clear(self): Removes all nodes from the queue, resetting its size to 0.
8. print(self): Prints the queue's size and content.

To use the QueueLL class, first, create an instance of the class:

```python
queue = QueueLL()
```

Then, create nodes and use the provided methods to manipulate the queue:

```python
node1 = SNode(1)
node2 = SNode(2)
node3 = SNode(3)

queue.enqueue(node1)
queue.enqueue(node2)
queue.enqueue(node3)

queue.print()
```

This will create a queue with three nodes and print its contents.

You can also use other methods to search, dequeue, and manipulate the queue as needed.

## Circular Doubly Linked List

The CDLL class is an implementation of a circular doubly-linked list that inherits from the DLL (Doubly Linked List) class. This class allows you to create and manipulate circular doubly-linked lists. The nodes in the list are connected in a circular fashion, with the tail node pointing to the head node and vice versa.

```python
from myLib import CDLL
from myLib import DNode
```

Here's a brief explanation of the methods provided by the CDLL class:

1. **init**(self, node=None): Initializes a new circular doubly-linked list. You can pass an optional node to set as the head of the list. This method also sets the prev pointer of the head node to the tail node and the next pointer of the tail node to the head node.
2. insert_head(self, node): Inserts a new node at the head of the list.
3. insert_tail(self, node): Inserts a new node at the tail of the list.
4. is_sorted(self): Checks if the list is sorted in ascending order.
5. sort(self): Sorts the list in ascending order using the bubble sort algorithm.
6. sorted_insert(self, node): Inserts a new node into the list while maintaining the sorted order.
7. search(self, node): Searches for a node in the list and returns it if found, otherwise returns None.
8. delete_head(self): Removes the head node from the list.
9. delete_tail(self): Removes the tail node from the list.
10. delete(self, node): Removes the specified node from the list.
11. print(self): Prints the list's length, sorted status, list content, and a loop back to the head.

To use the CDLL class, first, create an instance of the class:

```python
clist = CDLL()
```

Then, create nodes and use the provided methods to manipulate the list:

```python
node1 = DNode(1)
node2 = DNode(2)
node3 = DNode(3)

clist.insert_head(node1)
clist.insert_tail(node2)
clist.sorted_insert(node3)

clist.print()
```

This will create a circular doubly-linked list with three nodes and print its contents.

You can also use other methods to search, delete, and manipulate the list as needed.
