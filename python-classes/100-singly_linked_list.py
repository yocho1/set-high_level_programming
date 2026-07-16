#!/usr/bin/python3
"""This module defines a Node and SinglyLinkedList class."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node attribute with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position."""
        new_node = Node(value)

        # If list is empty or value is smaller than head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Find the correct position
        current = self.__head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return string representation of the list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
