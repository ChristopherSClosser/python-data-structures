"""Deque."""
from dll import DLL


class Deque(DLL):
    """Make a dequeue."""

    def appendleft(self, val):
        """Add new node to head of dequeue."""
        super(Deque, self).push(val)

    def pop(self):
        """Remove a value at end of dequeue and return value."""
        return super(Deque, self).shift()

    def popleft(self):
        """Remove a value at the head of deque and return it."""
        if not self.head:
            raise IndexError('cannot peekleft on an empty deque')
        if self.head:
            return super(Deque, self).pop()

    def peek(self):
        """Return value of tail."""
        if not self.tail:
            raise IndexError('cannot peek on an empty deque')
        return self.tail.val

    def peekleft(self):
        """Return value of head."""
        if not self.head:
            raise IndexError('cannot peekleft on an empty deque')
        return self.head.val
