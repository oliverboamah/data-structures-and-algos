class Node:
    """
    This class represents an element(node) in a linked list.

    Attributes:
        data: The value of the node
        next: The reference to the next node in the linked list
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
