"""Binary search tree class."""


class Node(object):
    """docstring for Node."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None
        self.level = None
        self.parent = None


class Bst(object):
    """docstring for Bst."""

    def __init__(self):
        """."""
        self.root = None
        self._size = 0

    def insert(self, val):
        """Insert a node into the tree."""
        if not self.root:
            self.root = Node(val)
            self._size += 1
            return
        current = self.root
        while True:
            if val < current.val:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(val)
                    self._size += 1
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    self._size += 1
                    break

    def search(self, val):
        """."""
        if self.root:
            node_found = self._search(val, self.root)
            if node_found:
                return node_found
            return None
        return None

    def _search(self, val, current):
        """."""
        if not current or not val:
            return None
        elif current.val == val:
            return current
        elif val < current.val:
            return self._search(val, current.left)
        else:
            return self._search(val, current.right)

    def size(self):
        """."""
        return self._size

    def depth(self, root):
        """."""
        if root is None:
            return 0
        else:
            return max(self.depth(root.left), self.depth(root.right)) + 1

    def contains(self, val):
        """."""
        if self._search(val, self.root):
            return True
        return False

    def balance(self, root):
        """."""
        if root is None:
            return 0
        else:
            return (self.depth(root.left)) - (self.depth(root.right))


def breadth_first_traversal(self, start_val):
    """."""
    if not self.search(start_val):
        yield 'node not found'
    current = self.search(start_val)
    yield current.val
    queue = [current.val]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
            yield current.left.val
        if current.right:
            queue.append(current.right)
            yield current.right.val
