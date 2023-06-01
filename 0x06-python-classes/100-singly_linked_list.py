#!/usr/bin/python3
"""Singly linked list"""


class Node:
    """Node class"""
    def __init__(self, data, next_node=None):
        """Initializes instances of the class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """getter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self):
        """Initializes instances of the class"""
        self.head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list"""
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                    value >= current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation of the objects"""
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
