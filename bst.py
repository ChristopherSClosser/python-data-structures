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

    # def delete(self, val):
    #     """."""
    #     return self.search(val), val

    def _min_node(self, node):
        """."""
        current = node
        while current.left:
            current = current.left
        return current

    def delete(self, val):
        """Delete a node of a given value from the bst.
        Replace deleted node with closest number to deleted node
        left most child of right neighbor, not right neighbor
        """

        del_node = self.search(val)
        if not del_node:
            raise ValueError('node not in tree')
        if del_node == self.root:
            if del_node.right:
                min_node = self._min_node(del_node.right)
                if min_node:
                    self.root = min_node
                else:
                    min_node = del_node.right
                    self.root = min_node
                    min_node.parent = None
                    if del_node.left:
                        min_node.left = del_node.left
                        del_node.left.parent = min_node

                min_node.parent = None
                del_node.right.parent = min_node
                min_node.right = del_node.right

            elif del_node.left:
                self.root = del_node.left
                
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



    # def _delete(self, node, val):
    #     """."""
    #     if not node.par
    #         if node.right and node.left:
    #             r_child = node.right
    #             l_child = node.left
    #             import pdb; pdb.set_trace()
    #             if node.parent:
    #                 if node.parent.left == l_child:
    #                     l_child.right = node.parent.right
    #                     node.parent.left = l_child.right
    #                     l_child.right.parent = node.parent
    #                     self.size -= 1
    #                     import pdb; pdb.set_trace()
    #                 else:
    #                     r_child.right = node.parent.left
    #                     node.parent.right = r_child.right
    #                     self.size -= 1
    #                     import pdb; pdb.set_trace()
    #                 node.parent.left = node.left
    #                 node.parent.right = node.right
    #                 self.size -= 1
    #             else:
    #                 # deleting root need to find smallest node in the rightsubtree make it the root relplace all pointers
    #
    #         else:
    #             if node.left:
    #                 node.parent.left = node.left
    #                 self.size -= 1
    #             else:
    #                 node.parent.right = node.right
    #                 self.size -= 1
    #     # else:
    #     #     if node.val > val:
    #     #         if node.left:
    #     #             node = node.left
    #     #             self._delete(node, val)
    #     #     elif node.val < val:
    #     #         if node.right:
    #     #             node = node.right
    #     #             self._delete(node, val)

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
