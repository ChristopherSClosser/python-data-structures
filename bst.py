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

    def delete(self, val):
        """."""
        if not self.root:
            return
        current = self.root
        return self._delete(current, val)

    def _min_node(self, node):
        """."""
        current = node
        while current.left:
            current = current.left

        return current

    def _delete(self, node, val):
        """."""
        if node:
            if val < node.val:
                node.left = self._delete(node.left, val)
            elif val > node.val:
                node.right = self._delete(node.right, val)
            else:
                if not node.left:
                    hold = node.right
                    node = None
                    return
                elif not node.right:
                    hold = node.left
                    node = None
                    return
                hold = self._min_node(node.right)
                node.val = hold.val
                node.right = self._delete(node.right, hold.val)

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

    def in_order(self, node):
        """."""
        if node:
            for val in self.in_order(node.left):
                yield val
            yield node.val
            for val in self.in_order(node.right):
                yield val

    def pre_order(self, node):
        """."""
        if node:
            yield node.val
            for val in self.pre_order(node.left):
                yield val
            for val in self.pre_order(node.right):
                yield val

    def post_order(self, node):
        """."""
        if node:
            for val in self.post_order(node.left):
                yield val
            for val in self.post_order(node.right):
                yield val
            yield node.val

    def breadth_first_traversal(self, val):
        """."""
        if not self.search(val):
            yield 'node not found'
        current = self.search(val)
        yield current.val
        queue = [current]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
                yield current.left.val
            if current.right:
                queue.append(current.right)
                yield current.right.val
