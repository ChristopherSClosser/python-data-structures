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
                    current.left.parent = current
                    self._size += 1
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(val)
                    current.right.parent = current
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

    def _min_node(self, node):
        """."""
        while node.left:
            node = node.left
        return node

    def _max_node(self, node):
        """."""
        while node.right:
            node = node.right
        return node

    def delete(self, val):
        """Delete a node of a given value from the bst."""

        del_node = self.search(val)
        if not del_node:
            raise ValueError('node not in tree')
        if del_node == self.root:
            if del_node.right:
                min_node = self._min_node(del_node.right)
                self.root = min_node
                min_node.parent = None
                del_node.right.parent = min_node
                min_node.right = del_node.right
                if del_node.left:
                    min_node.left = del_node.left
                    del_node.left.parent = min_node

                return  # Done deal with depth and size

            elif del_node.left:
                max_node = self._max_node(del_node.left)
                self.root = max_node
                del_node.left.parent = max_node



            return
        direction = ""
        if del_node.parent.right is del_node:
            direction = "right"
        else:
            direction = "left"
        if direction == "right":
            if not del_node.right and not del_node.left:
                """Del Node has no children."""
                del_node.parent.right = None
                del_node.parent = None
            elif del_node.right and not del_node.left:
                """Del Node has only right child."""
                del_node.parent.right = del_node.right
                del_node.right.parent = del_node.parent
            elif del_node.left and not del_node.right:
                """Del Node has only left child."""
                del_node.parent.right = del_node.left
                del_node.left.parent = del_node.parent
            else:
                """Del Node has both left and right children."""
                del_node.parent.right = del_node.right
                del_node.right.parent = del_node.parent
                min_node = self._min_node(del_node.right)
                if min_node is None:
                    min_node = del_node.right
                min_node.left = del_node.left
                del_node.left.parent = min_node
        if direction == "left":
            if del_node.right is None and del_node.left is None:
                """Del Node has no children."""
                del_node.parent.left = None
                del_node.parent = None
            elif del_node.right and not del_node.left:
                """Del Node has only right child."""
                del_node.parent.left = del_node.right
                del_node.right.parent = del_node.parent
            elif del_node.left and not del_node.right:
                """Del Node has only left child."""
                del_node.parent.left = del_node.left
                del_node.left.parent = del_node.parent
            else:
                """Del Node has both left and right children."""
                del_node.parent.left = del_node.right
                del_node.right.parent = del_node.parent
                min_node = self._min_node(del_node.right)
                if min_node is None:
                    min_node = del_node.right
                min_node.left = del_node.left
                del_node.left.parent = min_node
        self._size -= 1

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
