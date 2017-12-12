"""."""

from dll import DLL
from que_ import Queue
import pdb


class Priorityq(DLL):
    """Class for priority queue."""

    def __init__(self):
        """Make a priority que."""
        self._priority = []
        self.lowest = 0

    def insert(self, val, priority=None):
        """."""
        if not priority:
            priority = self.lowest
        if priority < self.lowest:
            self.lowest = priority
        for queue in self._priority:
            if priority == queue.priority:
                queue.enqueue(val)
                return
        q = Queue(priority)
        q.enqueue(val)
        for idx, queue in enumerate(self._priority):
            if priority > self._priority[idx].priority:
                self._priority.insert(idx, q)
                return
        self._priority.append(q)

    def peek(self):
        """Return next item to be dequeued."""
        try:
            return self._priority[0].head.val
        except IndexError:
            pass

    def pop(self):
        """Remove highest in q and return value."""
        if self.peek():
            res = self._priority[0].dequeue()
            if len(self._priority[0]) == 0:
                del self._priority[0]
            return res
        raise IndexError('Cannot pop from an empty q.')
