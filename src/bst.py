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
        if self.search(val):
            raise ValueError('node already exists')
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

    def delete(self, val):
        """Delete a node of a given value from the bst."""
        del_node = self.search(val)
        if not del_node:
            raise ValueError('node not in tree')
        if del_node == self.root:
            self._delete_root(del_node)
            return
        elif del_node.right:
            self._del_right_min(del_node)
            return
        elif del_node.left:
            self._del_left_max(del_node)
            return
        else:
            self._del_no_child(del_node)
        return

    def _min_node(self, node):
        """Find node with min val."""
        while node.left:
            node = node.left
        return node

    def _max_node(self, node):
        """Find node with max val."""
        while node.right:
            node = node.right
        return node

    def _delete_root(self, node):
        """Delete if root."""
        del_node = node
        if del_node.right:
            min_node = self._min_node(del_node.right)
            self.root = min_node
            min_node.parent = None
            if min_node == del_node.right.left:
                if min_node.right:
                    del_node.right.left = min_node.right
                else:
                    del_node.right.left = None
                del_node.right.parent = min_node
                min_node.right = del_node.right
            if del_node.left:
                min_node.left = del_node.left
                del_node.left.parent = min_node
            del_node = None
            self._size -= 1
            return
        elif del_node.left:
            max_node = self._max_node(del_node.left)
            self.root = max_node
            max_node.parent = None
            if max_node == del_node.left.right:
                if max_node.left:
                    del_node.left.right = max_node.left
                else:
                    del_node.left.right = None
            del_node.left.parent = max_node
            max_node.left = del_node.left
            del_node = None
            self._size -= 1
            return
        else:
            del_node = None
            self.root = None
            self._size = 0

    def _del_right_min(self, node):
        """If node to delete has right child."""
        del_node = node
        min_node = self._min_node(del_node.right)
        min_node.parent = del_node.parent
        if min_node == del_node.right.left:
            del_node.parent.right = min_node
            if del_node.left:
                min_node.left = del_node.left
                del_node.left.parent = min_node
                if min_node.right:
                    del_node.right.left = min_node.right
                    min_node.right.parent = del_node.right
                    min_node.right = del_node.right
                    del_node.right.parent = min_node
                    del_node = None
                    self._size -= 1
                    return
                else:
                    min_node.right = del_node.right
                    del_node.right.parent = min_node
                    del_node.right.left = None
                    del_node = None
                    self._size -= 1
                    return
            else:
                if min_node.right:
                    del_node.right.left = min_node.right
                    min_node.right.parent = del_node.right
                    min_node.right = del_node.right
                    del_node.right.parent = min_node
                    del_node = None
                    self._size -= 1
                    return
                min_node.right = del_node.right
                del_node.right.parent = min_node
                del_node = None
                self._size -= 1
                return
        elif min_node == del_node.right:
            """min node has no left"""
            # import pdb; pdb.set_trace()
            min_node.parent = del_node.parent
            del_node.parent.right = min_node
            if del_node.left:
                min_node.left = del_node.left
                del_node.left.parent = min_node
                del_node = None
                self._size -= 1
                return
            del_node = None
            self._size -= 1
            return

        del_node.right.parent = min_node
        min_node.right = del_node.right
        if del_node.left:
            min_node.left = del_node.left
            del_node.left.parent = min_node
        del_node = None
        self._size -= 1

    def _del_left_max(self, node):
        """If node has no right child or right child has only one sibling."""
        # import pdb; pdb.set_trace()

        del_node = node
        max_node = self._max_node(del_node.left)
        max_node.parent = del_node.parent
        if max_node == del_node.left.right:
            del_node.parent.left = max_node
            if del_node.right:
                del_node.right.parent = max_node
                max_node.right = del_node.right
                if max_node.left:
                    del_node.left.right = max_node.left
                    max_node.left.parent = del_node.left
                    max_node.left = del_node.left
                    del_node.left.parent = max_node
                    del_node = None
                    self._size -= 1
                    return
                else:
                    max_node.left = del_node.left
                    del_node.left.parent = max_node
                    del_node.left.right = None
                    del_node = None
                    self._size -= 1
                    return
            else:
                if max_node.left:
                    del_node.left.right = max_node.left
                    max_node.left.parent = del_node.left
                    max_node.left = del_node.left
                    del_node.left.parent = max_node
                    del_node = None
                    self._size -= 1
                    return
                max_node.left = del_node.left
                del_node.left.parent = max_node
                del_node = None
                self._size -= 1
                return
        elif max_node == del_node.left:
            """max node has no right"""
            # import pdb; pdb.set_trace()
            max_node.parent = del_node.parent
            del_node.parent.left = max_node
            if del_node.right:
                max_node.right = del_node.right
                del_node.right.parent = max_node
                del_node = None
                self._size -= 1
                return
            del_node = None
            self._size -= 1
            return

        del_node.left.parent = max_node
        max_node.left = del_node.left
        if del_node.right:
            max_node.right = del_node.right
            del_node.right.parent = max_node
        del_node = None
        self._size -= 1

    def _del_no_child(self, node):
        """If node to delete has no child."""
        del_node = node
        if del_node.parent.right == del_node:
            del_node.parent.right = None
        else:
            del_node.parent.left = None
        del_node = None
        self._size -= 1
        return

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

    def in_order(self, node):
        """Return generator with nodes ordered from least to greatest."""
        if node:
            for val in self.in_order(node.left):
                yield val
            yield node.val
            for val in self.in_order(node.right):
                yield val

    def pre_order(self, node):
        """Return generator with nodes starting left and down."""
        if node:
            yield node.val
            for val in self.pre_order(node.left):
                yield val
            for val in self.pre_order(node.right):
                yield val

    def post_order(self, node):
        """Return generator with nodes starting down and left."""
        if node:
            for val in self.post_order(node.left):
                yield val
            for val in self.post_order(node.right):
                yield val
            yield node.val

    def breadth_first_traversal(self, val):
        """Return generator list nodes left to right and down."""
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


if __name__ == '__main__':
    import random
    for i in range(20):
        nums = random.sample(range(1, 100), 99)
        test = Bst()
        for i in nums:
            test.insert(i)
        test.delete(nums.pop(random.randint(1, 99)))
        print('list of nums inserted into tree', sorted(nums))
        gen = test.in_order(test.root)
        print('gen', list(gen))
        # for i in range(120):
        #     print('gen', next(gen), '\n')


# if __name__ == '__main__':
#     import random
#     errcount = 0
#     for i in range(100):
#         try:
#             nums = random.sample(range(1, 100), 99)
#             test = Bst()
#             for i in nums:
#                 test.insert(i)
#             test.delete(nums.pop(random.randint(1, 100)))
#             gen = test.in_order(test.root)
#             res = [i for i in gen]
#             if sorted(nums) != res:
#                 errcount += 1
#                 print('No error raised, but results still uneven. Likely dropped child')
#
#         except:
#             errcount += 1
#     print(errcount)
