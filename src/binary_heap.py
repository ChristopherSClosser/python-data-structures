"""Implementation of min heap."""


class Binheap(object):
    """Binary min heap."""

    def __init__(self, iterable=None):
        """."""
        self.container = []
        self._tailidx = -1
        if isinstance(iterable, (str, tuple, list)):
            for i in iterable:
                self.push(i)

    def push(self, val):
        """Add new value."""
        self._tailidx += 1
        self.container.append(val)
        self._shiftup(self._tailidx)

    def pop(self):
        """Remove head by bubbling down and removing and returning the val."""
        if self._tailidx == -1:
            raise IndexError('Cannot pop from an empty list')
        min_val = self.container[0]
        self.container[0] = self.container[self._tailidx]
        self._tailidx -= 1
        self._shiftdown(0)
        return min_val

    def _shiftup(self, idx):
        """Go through container swapping values."""
        while idx > 0:
            parent_idx, parent_val = self._parent(idx)
            if parent_val <= self.container[idx]:
                break
            self.container[parent_idx], self.container[idx] = self.container[idx], self.container[parent_idx]
            idx = parent_idx

    def _shiftdown(self, idx):
        """Go through container and swaps if parent is greater than child."""
        while True:
            idx_val = self.container[idx]

            left_idx, left_val = self._leftchild(idx, idx_val)
            right_idx, right_val = self._rightchild(idx, idx_val)
            if idx_val <= left_val and idx_val <= right_val:
                break

            if left_val < right_val:
                new_idx = left_idx
            else:
                new_idx = right_idx
            self.container[new_idx], self.container[idx] = self.container[idx], self.container[new_idx]
            idx = new_idx

    def _parent(self, idx):
        """Find parent given child."""
        if idx == 0:
            return None, None

        parent_idx = (idx - 1) // 2
        return parent_idx, self.container[parent_idx]

    def _leftchild(self, idx, default_val):
        """Find left child given parent."""
        child_idx = 2 * idx + 1
        if child_idx > self._tailidx:
            return None, default_val
        return child_idx, self.container[child_idx]

    def _rightchild(self, idx, default_val):
        """Find right child given parent."""
        child_idx = 2 * idx + 2
        if child_idx > self._tailidx:
            return None, default_val
        return child_idx, self.container[child_idx]
