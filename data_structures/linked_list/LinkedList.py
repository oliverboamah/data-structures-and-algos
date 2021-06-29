from node import Node


class LinkedList:
    """
    This class represents the linked list data structure

    Attributes:
        head: Holds the first node(element) in the linked list
        tail: Holds the last node(element) in the linked list
        size: Holds the number of nodes(elements) in the linked list
    """

    def __init__(self, data_structure='linked list'):
        self.head = None
        self.tail = None
        self.size = 0
        self.data_structure = data_structure
        self.errors = {
            'EMPTY': f'There are no elements in the {self.data_structure}',
            'INDEX_OUT_OF_RANGE': f'Index out of range: '
        }

    """
    Big O Time Complexity(Worst case) => O(N)
    Big O Space Complexity(Worst case) => O(1)
    """
    def __str__(self):
        values = None
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
            values += f', {current_node.data}'

        values = f'[{values}]'

        return values

    """
    Add a value to tail of the linked list
    Big O Time Complexity(Worst case) => O(1)
    Big O Space Complexity(Worst case) => O(1)
    """
    def add_tail(self, value):
        if self.size == 0:
            self.head = Node(data=value)
        else:
            new_node = Node(data=value)

            if self.size == 1:
                self.tail = new_node
                self.head.next = self.tail
            else:
                self.tail.next = new_node
                self.tail = new_node

        self.size += 1

    """
    Add a value to the head of the linked list
    Big O Time Complexity(Worst case) => O(1)
    Big O Space Complexity(Worst case) => O(1)
    """
    def add_head(self, value):
        new_node = Node(data=value)

        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1

    """
    Check if the linked list contains a value
    Return True if the specified value is found, else return False
    Big O Time Complexity(Worst case) => O(N)
    Big O Space Complexity(Worst case) => O(1)
    """
    def contains(self, value):
        if self.size == 0:
            return False

        current_node = self.head
        while current_node.next is not None:
            if current_node.data == value:
                return True

            current_node = current_node.next

    """
    Insert a value at a specified index in the linked list
    Big O Time Complexity(Worst case) => O(N)
    Big O Space Complexity(Worst case) => O(1)
    """
    def insert(self, index, value):
        new_node = Node(data=value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

        if index == self.size:
            self.add_tail(value=value)
            return

        else:
            current_node = self.head
            for number in range(index):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

        self.size += 1

    """
    Get the value at the specified index in the linked list
    Big O Time Complexity(Worst case) => O(N)
    Big O Space Complexity(Worst case) => O(1)
    """
    def get(self, index):

        if index >= self.size:
            raise IndexError(self.errors.get('INDEX_OUT_OF_RANGE') + str(index))

        else:
            current_node = self.head
            for number in range(index):
                current_node = current_node.next

            return current_node

    """
    Remove a value at the specified index in the linked list
    Big O Time Complexity(Worst case) => O(N)
    Big O Space Complexity(Worst case) => O(1)
    """
    def remove(self, index):
        if index >= self.size:
            raise IndexError(self.errors.get('INDEX_OUT_OF_RANGE') + str(index))
        elif index == 0 and size == 1:
            self.head = None
        else:
            current_node = self.head
            for number in range(index - 1):
                current_node = current_node.next

            node_to_delete = current_node.next
            current_node.next = node_to_delete.next
            node_to_delete = None

        size -= 1

    """
    Remove the value from the head of the linked list
    Big O Time Complexity(Worst case) => O(1)
    Big O Space Complexity(Worst case) => O(1)
    """
    def remove_head(self):
        if self.size == 0:
            raise Exception(self.errors.get('EMPTY'))
        elif size == 1:
            self.head = None
        else:
            node = self.head
            self.head = self.head.next
            node = None

        self.size -= 1

    """
    Remove the value from the tail of the linked list
    Big O Time Complexity(Worst case) => O(N)
    Big O Space Complexity(Worst case) => O(1)
    """
    def remove_tail(self, return_value=False):

        if self.size == 0:
            raise Exception(self.errors.get('EMPTY'))
        elif size == 1:
            value = self.head.data
            self.head = None
        else:
            value = self.tail.data
            self.tail = None

            current_node = self.head
            while current_node.next != null:
                current_node = current_node

            self.tail = current_node

        self.size -= 1

        return value if return_value else None
