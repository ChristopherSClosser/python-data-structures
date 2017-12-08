"""Trie tree."""


class Node(object):
    """Node for a Trie tree."""

    def __init__(self, val, parent=None):
        """Create a node with the given value."""
        self.val = val
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

    def contains(self, word):
        """Check if the given word is in the Trie tree."""
        if not isinstance(word, str):
            raise TypeError('Can only check for words in the trie.')

        current = self.root
        for char in word + '$':
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def size(self):
        """Get the number of words in the Trie tree."""
        return self._size

    def remove(self, word):
        """Remove the given word from the Trie tree."""
        if not isinstance(word, str):
            raise TypeError('You can only remove a word from the trie.')

        current = self.root
        for char in word + '$':
            if char not in current.children:
                raise ValueError('The word is not in the trie.')
            current = current.children[char]

        current = current.parent
        last_char = '$'
        while len(current.children) == 1 and current.val != '*':
            last_char = current.val
            current = current.parent

        del current.children[last_char]
        self._size -= 1
