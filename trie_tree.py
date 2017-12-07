"""Trie tree."""


class Node(object):
    """Node for a Trie tree."""

    def __init__(self, value, parent=None):
        """Create a node with the given value."""
        self.val = value
        self.parent = parent
        self.children = {}


class Trie(object):
    """Trei tree."""

    def __init__(self, iterable=None):
        """Create an empty Trie tree."""
        self.root = Node('*')
        self._size = 0

        if isinstance(iterable, (list, tuple)):
            for item in iterable:
                self.insert(item)
        elif iterable is not None:
            raise TypeError('Iterable must be a list, or tuple.')

    def insert(self, word):
        """Insert word into the tree, duplicate characters ignored."""
        if not isinstance(word, str):
            raise TypeError('Can only insert words into the trie.')

        current = self.root
        for char in word:
            current.children.setdefault(char, Node(char, current))
            current = current.children[char]

        new_end = Node('$', current)
        set_end = current.children.setdefault('$', new_end)
        if set_end is new_end:
            self._size += 1
