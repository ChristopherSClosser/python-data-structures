"""Implementation of a que."""

from dll import DLL


class Queue(DLL):
    """Makes a queue."""

    def __init__(self, priority=None):
        """."""
        super(Queue, self).__init__()
        self.priority = priority

    def enqueue(self, value):
        """Enqueue method for queue."""
        super(Queue, self).append(value)

    def dequeue(self):
        """Remove head and return val."""
        return super(Queue, self).pop()

    def peek(self):
        """Return the value of the first item in queue."""
        return self.head.val
