"""Test trie."""

import pytest
from trie_tree import Node, Trie


with open('/usr/share/dict/words') as f:
    DICT_LIST = [word.strip() for word in f]


@pytest.fixture
def trie():
    """Make an empty trei tree."""
    return Trie()


@pytest.fixture
def node():
    """Make a new node."""
    return Node(1)


def test_node_childeren_empty_dict(node):
    """."""
    assert node.children == {}


def test_node_val(node):
    """."""
    assert node.val == 1


def test_node_parent(node):
    """."""
    assert node.parent is None


def test_trie_size(trie):
    """."""
    trie.insert('money')
    assert trie.size() == 1
    trie.insert('monkey')
    assert trie.size() == 2
