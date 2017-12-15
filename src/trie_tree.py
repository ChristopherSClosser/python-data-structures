"""Trie tree."""


class Node(object):
    """Node for a Trie tree."""

    def __init__(self, val, parent=None, next=None):
        """Create a node with the given value."""
        self.val = val
        self.parent = parent
        self.next = next
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

    def traverse(self, ichar=''):
        """."""
        if not isinstance(ichar, str):
            raise TypeError('must be a letter or empty string, ""')

        def depth(node, init):
            """Get all node vals depth first."""
            if not node:
                return
            if node.val != '*' and node.val != '$' and not init:
                yield node.val
            for child in node.children:
                for val in depth(node.children[child], False):
                    yield val
        current = self.root
        for child in ichar:
            if child not in current.children:
                current = None
                break
            current = current.children[child]
        return depth(current, True)

    def autosearch(self, string, sofar=""):
        """Perform auto completion search and print the autocomplete results."""
        if len(string) > 0:
            key = string[0]
            string = string[1:]
            if key in self.next:
                sofar = sofar + key
                self.next[key].search(string, sofar)
            else:
                print "No match"
        else:
            if self.val == '$':
                print "Match:", sofar

            for key in self.next.keys():
                self.next[key].traverse(sofar + key)


def fileparse(filename):
    """Parse the input dictionary file and build the trie data structure."""
    fd = open(filename)

    root = Node()
    line = fd.readline().strip('\r\n')

    while line != '':
        root.add_item(line)
        line = fd.readline().strip('\r\n')

    return root


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print "Usage: ", sys.argv[0], "dictionary_file.txt"
        sys.exit(2)

    root = fileparse(sys.argv[1])

    print "Input:",
    input=raw_input()
    root.search(input)
