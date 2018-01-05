"""Implementation of a stack."""

from linked_list import LinkedList


class Stack(object):
    """Class for a stack."""

    def __init__(self, iterable=None):
        """Function to create an instance of a stack."""
        self.length = 0
        self._stack = LinkedList()
        self.top = None
        if isinstance(iterable, (str, tuple, list)):
            for i in iterable:
                self.push(i)

    def pop(self):
        """Use LinkedList pop method."""
        """Remove the head of the list and return it."""
        if self.top is None:
            raise IndexError("List is empty, cannot pop from an empty list")
        val = self.top.val
        self.top = self.top.next_node
        self.length -= 1
        return val

    def push(self, val):
        """Use push method from LinkedList."""
        self._stack.push(val)
        self.top = self._stack.head

    def __len__(self):
        """Redifine the built in len function for the list."""
        return self._stack.length
