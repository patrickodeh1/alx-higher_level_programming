#!/usr/bin/python3

"""Defines a class node"""


class Node():
    """singly linked list node"""

    def __init__(self, data, next_node=None):
        """initializer"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the value for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieves next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the value for the next node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""defines a class SinglyLinkedList"""


class SinglyLinkedList():
    """linked list"""
    def __init__(self):
        """Initializes self"""
        self.head = None

    def sorted_insert(self, value):
        """inserts sorted value"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """str"""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
