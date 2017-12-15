"""Test dequeue."""
from dequeue import Deque
import pytest


@pytest.fixture
def dq():
    """Make an empty dequeue."""
    return Deque()


def test_dequeue(dq):
    """Test append to tail."""
    dq.append(2)
    assert dq.tail.val == 2


def test_dequeue_pop_single_tail_none(dq):
    """Test pop from single list then no tail."""
    dq.append(1)
    dq.pop()
    assert dq.tail is None


def test_dequeue_pop_single_head_none(dq):
    """Test pop from single list then no head."""
    dq.append(1)
    dq.pop()
    assert dq.head is None


def test_dequeue_popleft_single_tail_none(dq):
    """Test pop from single list then no tail."""
    dq.append(1)
    dq.popleft()
    assert dq.tail is None


def test_dequeue_popleft_single_head_none(dq):
    """Test pop from single list then no head."""
    dq.append(1)
    dq.popleft()
    assert dq.head is None


def test_append_left(dq):
    """Test that append left adds value to the head."""
    dq.appendleft(1)
    dq.appendleft(2)
    assert dq.head.val == 2


def test_pop_removes_tail(dq):
    """Test_pop_removes_tail."""
    dq.append(2)
    dq.append(1)
    dq.append(3)
    assert dq.pop() == 3


def test_pop_raises_error_with_empty_deque(dq):
    """Raise an index error when pop from empty deque."""
    with pytest.raises(IndexError):
        dq.pop()


def test_popleft_raises_error_with_empty_deque(dq):
    """Raise an index error when popleft from empty deque."""
    with pytest.raises(IndexError):
        dq.popleft()


def test_peek_raises_error_with_empty_deque(dq):
    """Raise an index error when peek from empty deque."""
    with pytest.raises(IndexError):
        dq.peek()


def test_peekleft_raises_error_with_empty_deque(dq):
    """Raise an index error when peekleft from empty deque."""
    with pytest.raises(IndexError):
        dq.peekleft()


def test_popleft_returns_head(dq):
    """Pop should remove and return head."""
    dq.append(2)
    dq.append(1)
    dq.append(3)
    assert dq.popleft() == 2


def test_popleft_returns_head_single_item(dq):
    """Popleft should remove and return head."""
    dq.append(2)
    assert dq.popleft() == 2


def test_pop_returns_head_single_item(dq):
    """Pop should remove and return head."""
    dq.append(2)
    assert dq.pop() == 2


def test_peek_returns_tail_single_item(dq):
    """Peek should return tail."""
    dq.append(2)
    assert dq.peek() == 2


def test_peekleft_returns_head_single_item(dq):
    """Peekleft should return head."""
    dq.append(2)
    assert dq.peekleft() == 2


def test_peek_returns_tail_val(dq):
    """Peek should return value of the tail."""
    dq.appendleft(3)
    dq.appendleft(2)
    dq.appendleft(1)
    assert dq.peek() == 3


def test_peekleft_returns_head_val(dq):
    """Peek should return value of the tail."""
    dq.appendleft(3)
    dq.appendleft(2)
    dq.appendleft(1)
    assert dq.peekleft() == 1


def test_dequeue_size_inherit(dq):
    """Test_dequeue_size_inherit."""
    dq.appendleft(3)
    dq.appendleft(2)
    dq.appendleft(1)
    assert dq.size() == 3


def test_dequeue_len_inherit(dq):
    """Test_dequeue_len_inherit."""
    dq.appendleft(3)
    dq.appendleft(2)
    dq.appendleft(1)
    assert len(dq) == 3


def test_dequeue_len_empty(dq):
    """Test length of empty dequeue is 0."""
    assert len(dq) == 0
