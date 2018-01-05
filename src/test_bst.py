"""Test for binary search tree."""

import pytest
from bst import Node, Bst
import random


@pytest.fixture
def bst():
    """Make an empty bst."""
    return Bst()


@pytest.fixture
def bst_2():
    """Make a bst with stuff."""
    bst = Bst()
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(7)
    return bst


@pytest.fixture
def node():
    """Make a new node."""
    return Node(1)


def test_bst_node_for_left_none(node):
    """test_bst_node_for_left_none."""
    assert node.left is None


def test_bst_root_none(bst):
    """test_bst_root_none."""
    assert bst.root is None


def test_bst_balance_none(bst):
    """test_bst_balance_none."""
    assert bst.balance(bst.root) == 0


def test_add_node_to_bst(bst):
    """test_add_node_to_bst."""
    bst.insert(1)
    assert bst.root.val == 1


def test_add_0_to_bst(bst):
    """test_add_node_to_bst."""
    # bst.insert(0)
    # assert bst.root.val == 0


def test_search_bst(bst):
    """test_search_bst."""
    bst.insert(1)
    assert bst.search(1).val == 1


def test_search_no_val_enterd_bst(bst_2):
    """test_search_bst."""
    # with pytest.raises(ValueError):
    #     bst_2.search()


def test_search_bst_node_not_in_tree(bst):
    """test_search_bst_node_not_in_tree."""
    bst.insert(1)
    assert bst.search(2) is None


def test_depth_on_0(bst):
    """test_depth_on_0."""
    assert bst.depth() == 0


def test_contains_bst_node(bst):
    """test_contains_bst_node."""
    bst.insert(1)
    assert bst.contains(1) is True


def test_contains_bst_node_not_in_tree(bst):
    """test_contains_bst_node_not_in_tree."""
    bst.insert(1)
    assert bst.contains(2) is False


def test_search_empty_tree(bst):
    """test_search_empty_tree."""
    assert bst.search(1) is None


def test_search_tree(bst_2):
    """test_search_tree."""
    assert bst_2.search(1).val == 1


def test_search_left(bst):
    """test_search_left."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(1)
    assert bst.search(2).val == 2


def test_add_nodes_to_bst_check_size(bst):
    """test_add_nodes_to_bst_check_size."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    assert bst._size == 5


def test_add_nodes_to_bst_check__size(bst):
    """test_add_nodes_to_bst_check__size."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    assert bst.size() == 5


def test_add_nodes_to_bst_check_depth(bst):
    """Test_add_nodes_to_bst_check_depth."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    assert bst.depth() == 3


def test_add_nodes_to_bst_check_balance(bst):
    """Test_add_nodes_to_bst_check_balance."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(7)
    assert bst.balance(bst.root) == -1


def test_add_nodes_to_bst_check_balance_0(bst):
    """Test_add_nodes_to_bst_check_balance_0."""
    bst.insert(3)
    bst.insert(5)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(7)
    # bst.insert(0)
    # assert bst.balance(bst.root) == 0


@pytest.mark.parametrize('nums', [num for num in range(1, 20)])
def test_sample_of_insertions_size(nums):
    """Test_sample_of_insertions_size."""
    items = random.sample(range(1, 100), 99)
    test = Bst()
    for num in items:
        test.insert(num)
    assert test.size() == 99


@pytest.mark.parametrize('nums', [num for num in range(1, 20)])
def test_search_random(bst_2, nums):
    """test_search_random."""
    find = random.sample(range(1, 7), 1)
    assert bst_2.search(find[0]).val == find[0]


def test_inorder(bst):
    """test_inorder."""
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(8)
    bst.insert(4)
    bst.insert(1)
    tree = bst.in_order(bst.root)
    res = list(tree)
    assert res == [1, 2, 3, 4, 5, 6, 7, 8]


def test_preorder(bst):
    """test_preorder."""
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(8)
    bst.insert(4)
    bst.insert(1)
    tree = bst.pre_order(bst.root)
    res = list(tree)
    assert res == [5, 3, 2, 1, 4, 6, 7, 8]


def test_postorder(bst):
    """test_postorder."""
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(8)
    bst.insert(4)
    bst.insert(1)
    tree = bst.post_order(bst.root)
    res = list(tree)
    assert res == [1, 2, 4, 3, 8, 7, 6, 5]


def test_breadth_first(bst):
    """test_breadth_first."""
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(8)
    bst.insert(4)
    bst.insert(1)
    tree = bst.breadth_first_traversal(bst.root.val)
    res = list(tree)
    assert res == [5, 3, 6, 2, 4, 7, 1, 8]


def test_breadth_first_no_val(bst):
    """test_breadth_first_no_val."""
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(3)
    bst.insert(2)
    bst.insert(8)
    bst.insert(4)
    bst.insert(1)
    tree = bst.breadth_first_traversal(9)
    assert next(tree) == 'node not found'


@pytest.mark.parametrize('nums', [num for num in range(1, 20)])
def test_inorder_multiple(nums):
    """test_inorder_multiple."""
    nums = random.sample(range(1, 100), 99)
    test = Bst()
    for i in nums:
        test.insert(i)
    nums = sorted(nums)
    gen = test.in_order(test.root)
    assert [i for i in gen] == nums


def test_delete_single_node(bst):
    """test_delete_single_node."""
    bst.insert(1)
    bst.delete(1)
    assert bst.root is None


def test_delete_root_only_three_nodes(bst):
    """test_delete_root_only_three_nodes."""
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.delete(2)
    tree = bst.pre_order(bst.root)
    tl = list(tree)
    assert tl == [3, 1]


def test_delete_right_min_with_right_child(bst):
    """test_delete_right_min_with_right_child."""
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.delete(4)
    bst.insert(2.5)
    bst.insert(2.6)
    bst.delete(2)
    tree = bst.pre_order(bst.root)
    tl = list(tree)
    # assert tl == [5, 2.5, 1, 3, 2.6, 6, 7]


def test_delete_left_max_with_left_child(bst):
    """test_delete_left_max_with_left_child."""
    bst.insert(4)
    bst.insert(2)
    bst.insert(6)
    bst.insert(1)
    bst.insert(3)
    bst.insert(5)
    bst.insert(7)
    bst.delete(4)
    bst.insert(2.5)
    bst.insert(2.6)
    bst.insert(4)
    bst.insert(2.55)
    bst.delete(3)
    tree = bst.pre_order(bst.root)
    tl = list(tree)
    # assert tl == [5, 2, 1, 2.6, 2.5, 2.55, 4, 6, 7]
