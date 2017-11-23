"""Test for binary search tree."""

import pytest
from bst import Node, Bst


@pytest.fixture
def bst():
    """Make an empty bst."""
    return Bst()


@pytest.fixture
def node():
    """Make a new node."""
    return Node(1)


def test_bst_node_for_left_none(node):
    """."""
    assert node.left is None


def test_bst_root_none(bst):
    """."""
    assert bst.root is None


def test_bst_balance_none(bst):
    """."""
    assert bst.balance(bst.root) == 0


def test_add_node_to_bst(bst):
    """."""
    bst.insert(1)
    assert bst.root.val == 1


def test_search_bst(bst):
    """."""
    bst.insert(1)
    assert bst.search(1).val == 1


def test_search_bst_node_not_in_tree(bst):
    """."""
    bst.insert(1)
    assert bst.search(2) is None


def test_contains_bst_node(bst):
    """."""
    bst.insert(1)
    assert bst.contains(1) is True


def test_contains_bst_node_not_in_tree(bst):
    """."""
    bst.insert(1)
    assert bst.contains(2) is False


def test_search_empty_tree(bst):
    """."""
    assert bst.search(1) is None


def test_search_left(bst):
    """."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    assert bst.search(2).val == 2


def test_add_nodes_to_bst_check_size(bst):
    """."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    assert bst._size == 5


def test_add_nodes_to_bst_check__size(bst):
    """."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    assert bst.size() == 5


def test_add_nodes_to_bst_check_depth(bst):
    """."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    assert bst.depth(bst.root) == 3


def test_add_nodes_to_bst_check_balance(bst):
    """."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(7)
    assert bst.balance(bst.root) == -1
