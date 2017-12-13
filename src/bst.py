"""Binary search tree class."""


class Node(object):
    """docstring for Node."""

    def __init__(self, val):
        """."""
        self.val = val
        self.left = None
        self.right = None
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
        """Return node in tree if found."""
        if not val:
            raise ValueError('you must enter a value to search')
        if self.root:
            node_found = self._search(val, self.root)
            if node_found:
                return node_found
            return None
        return None

    def _search(self, val, current):
        """Helper for search."""
        if not current:
            return None
        elif current.val == val:
            return current
        elif val < current.val:
            return self._search(val, current.left)
        else:
            return self._search(val, current.right)

    def size(self):
        """Return number of nodes in tree."""
        return self._size

    def depth(self):
        """Return overall depth of tree."""
        if not self.root:
            return 0
        else:
            return self._depth(self.root)

    def _depth(self, root):
        """Helper for depth."""
        if not root:
            return 0
        else:
            return max(self._depth(root.left), self._depth(root.right)) + 1

    def contains(self, val):
        """Return true if node with val is in tree."""
        if self._search(val, self.root):
            return True
        return False

    def balance(self, root):
        """Return the difference in depth of left and right subtrees."""
        if root is None:
            return 0
        else:
            return (self._depth(root.left)) - (self._depth(root.right))
