"""Defines a class node"""
class Node():
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
        if value is type(Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

"""defines a class SinglyLinkedList"""
class SinglyLinkedList():
    def __init__(self, head):
        """Initializes self"""
        self.head = head

