"""Test double linked list."""

import pytest
from dll import DLL
from linked_list import Node


@pytest.fixture
def new_dll():
    """Create a new double linked list."""
    new_dll = DLL()
    return new_dll


def test_dll_on_init_has_tail(new_dll):
    """Test_dll_on_init_has_tail."""
    assert hasattr(new_dll, 'tail')


def test_push_to_dll(new_dll):
    """Test for push method, two items."""
    new_dll.push(1)
    new_dll.push(2)
    assert new_dll.head.val == 2
# test for head.val == tail.val


def test_push_to_empty_dll(new_dll):
    """Test for push method no items."""
    new_dll.push(1)
    assert new_dll.head.val == 1


def test_push_to_dll_next(new_dll):
    """Test to push value changes head.next."""
    new_dll.push(1)
    new_dll.push(2)
    assert new_dll.head.next_node.val == 1


def test_push_to_dll_prev(new_dll):
    """Test for push method affecting previous values."""
    new_dll.push(1)
    new_dll.push(2)
    assert new_dll.head.next_node.prev_node.val == 2


def test_new_dll_head_is_none(new_dll):
    """Test if dll head is empty on init."""
    assert new_dll.head is None


def test_new_dll_tail_is_none(new_dll):
    """Test if dll tail is empty on init."""
    assert new_dll.tail is None


def test_node_has_prev_pointer():
    """Test for node previous pointer."""
    test_node = Node(1)
    assert test_node.prev_node is None


def test_pop_returns_removes_and_returns_head(new_dll):
    """Test_pop_returns_removes_and_returns_head."""
    new_dll.push(1)
    new_dll.push(2)
    new_dll.push(4)
    res = new_dll.pop()
    assert res == 4


def test_pop_next_val(new_dll):
    """Test_pop_affect next pointer."""
    new_dll.push(1)
    new_dll.push(2)
    new_dll.push(4)
    new_dll.pop()
    assert new_dll.head.next_node.val == 1


def test_pop_prev_val(new_dll):
    """Test_pop_affect previous pointer."""
    new_dll.push(1)
    new_dll.push(2)
    new_dll.push(4)
    new_dll.pop()
    assert new_dll.head.next_node.prev_node.val == 2


def test_remove_node_from_list(new_dll):
    """Test_remove_node_from_list."""
    new_dll.push(3)
    new_dll.push(2)
    new_dll.push(1)
    new_dll.remove(2)
    assert new_dll.tail.prev_node.val == 1


def test_append_to_dll(new_dll):
    """Test for append method."""
    new_dll.push(2)
    new_dll.push(1)
    new_dll.append(3)
    assert new_dll.tail.val == 3


def test_append_to_dll_prev(new_dll):
    """Test for append method."""
    new_dll.push(2)
    new_dll.push(1)
    new_dll.append(3)
    assert new_dll.tail.prev_node.val == 2


def test_append_to_dll_next(new_dll):
    """Test for append method."""
    new_dll.push(2)
    new_dll.push(1)
    new_dll.append(3)
    assert new_dll.head.next_node.val == 2


def test_append_to_empty_dll(new_dll):
    """Test for append method."""
    new_dll.append(3)
    assert new_dll.tail.val == 3


def test_shift_removes_tail(new_dll):
    """Test_shift_removes_tail."""
    new_dll.push(2)
    new_dll.push(1)
    new_dll.append(3)
    assert new_dll.shift() == 3


def test_remove_no_value_raise_error(new_dll):
    """Remove on empty dll should raise exception."""
    with pytest.raises(IndexError):
        new_dll.remove(2)


def test_remove_no_value_specified_raise_error(new_dll):
    """Remove on empty dll should raise exception."""
    new_dll.push(2)
    with pytest.raises(TypeError):
        new_dll.remove()


def test_shift_removes_tail_prev_pointer(new_dll):
    """Test_shift_removes_tail_affect_prev_correctly."""
    new_dll.push(2)
    new_dll.push(1)
    new_dll.append(3)
    new_dll.shift()
    assert new_dll.tail.prev_node.val == 1


def test_shift_removes_tail_next_pointer(new_dll):
    """Test_shift_removes_tail_affect_next_correctly."""
    new_dll.push(2)
    new_dll.push(1)
    new_dll.shift()
    assert new_dll.head.next_node is None


def test_pop_empty_dll_raises_error(new_dll):
    """Pop should raise index error on empty dll."""
    with pytest.raises(IndexError):
        new_dll.pop()


def test_shift_empty_dll_raises_error(new_dll):
    """Pop should raise index error on empty dll."""
    with pytest.raises(IndexError):
        new_dll.shift()


def test_remove_no_value_specified_raise_value_error(new_dll):
    """Remove on empty dll should raise exception."""
    new_dll.push(2)
    with pytest.raises(TypeError):
        new_dll.remove()


def test_remove_for_head_val(new_dll):
    """Remove a value that isnt the head."""
    new_dll.push(1)
    new_dll.push(2)
    new_dll.push(3)
    new_dll.remove(3)
    assert new_dll.head.val == 2
