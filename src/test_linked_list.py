"""Test linked list."""
from linked_list import LinkedList, Node
import pytest


def test_push():
    """Test for push method."""
    res = LinkedList()
    res.push(2)
    assert res.head.val == 2


def test_push_two_items():
    """Test for push method."""
    res = LinkedList()
    res.push(2)
    res.push(3)
    assert res.head.val == 3


def test_push_two_items_head_next():
    """Test for push method."""
    res = LinkedList()
    res.push(2)
    res.push(3)
    assert res.head.next_node.val == 2


def test_node():
    """Test for node."""
    test_node = Node(1)
    assert test_node.val == 1


def test_init_list():
    """"test_init_list."""
    init = LinkedList()
    assert init.head is None


def test_empty_list_length():
    """Test size() on empty list."""
    test_list = LinkedList()
    assert test_list.size() == 0


def test_length_with_two_nodes():
    """test_length_with_two_nodes."""
    test_list = LinkedList()
    test_list.push(2)
    test_list.push(3)
    assert test_list.size() == 2


def test_empty_list_length_with_len():
    """Test size() on empty list using len method."""
    test_list = LinkedList()
    assert len(test_list) == 0


def test_display():
    """test_display."""
    test_list = LinkedList()
    test_list.push(1)
    test_list.push(2)
    test_list.push(3)
    assert test_list.display() == '(3, 2, 1)'


def test_str():
    """test_display."""
    test_list = LinkedList()
    test_list.push(1)
    test_list.push(2)
    test_list.push(3)
    assert test_list.__str__() == '(3, 2, 1)'


def test_linked_list_pop_removes_head():
    """Test to see if pop method removes the current head."""
    ll = LinkedList()
    ll.push(1)
    ll.pop()
    assert ll.head is None


def test_linked_list_pop_two_vals():
    """Test to see if pop method removes the current head."""
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.pop()
    assert ll.head.val == 1


def test_linked_list_pop_three_vals_next_works():
    """Test to see if pop method removes the current head."""
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.push(3)
    ll.pop()
    assert ll.head.next_node.val == 1


def test_linked_list_search_returns_node_if_exists():
    """Test_linked_list_search_returns_node_if_exists."""
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    assert ll.search(1) == ll.head.next_node


def test_remove_removes_node():
    """Test to see if remove removes a given node."""
    ll = LinkedList()
    ll.push(1)
    ll.push(2)
    ll.remove(ll.head.next_node)
    assert ll.head.next_node is None


def test_remove_raises_exception_when_node_not_found():
    """Test that exception is raised when node isn't found."""
    ll = LinkedList()
    assert ll.remove(ll.head) == "Node was not found in list"


def test_pop_raises_exception_when_node_not_found():
    """Test that exception is raised when node isn't found."""
    ll = LinkedList()
    assert ll.pop() == "List is empty, cannot pop from an empty list"


def test_linkedlist_take_iterable():
    """Test that LinkedList can take an iterable."""
    tlist = [5, 4, 3, 2, 1]
    ll = LinkedList(tlist)
    for item in tlist:
        assert ll.search(item).val == item


def test_ll_search_one_val():
    """Test search method with one node."""
    ll = LinkedList()
    ll.push(2)
    assert ll.search(2).val == 2
