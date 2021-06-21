from node import Node


class LinkedList:
    """
    This class represents the linked list data structure

    Attributes:
        head: Holds the first node(element) in the linked list
        tail: Holds the last node(element) in the linked list
        size: Holds the number of nodes(elements) in the linked list
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    """
    Add a value to the linked list
    """
    def add(self, value):
        if self.size == 0:
            self.head = Node(data=value)
        else:
            node = Node(data=value)

            if self.size == 1:
                self.tail = node
                self.head.next = self.tail
            else:
                self.tail.next = node
                self.tail = node

        self.size += 1

    """
    Check if the linked list contains a value
    Return True if the specified value is found, else return False
    """
    def contains(self, value):
        if self.size == 0:
            return False

        current_node = self.head
        while current_node.next is not None:
            if current_node.data == value:
                return True

            current_node = current_node.next
