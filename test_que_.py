"""Test for queue module."""

from que_ import Queue
import pytest


@pytest.fixture
def new_queue():
    """Make an empty queue."""
    q = Queue()
    return q


@pytest.fixture
def full_q():
    """Make q with stuff in it."""
    q = Queue([4, 3, 2, 1])
    return q


def test_enqueue(new_queue):
    """Test to see that tail has correct val after enqueue."""
    new_queue.enqueue(2)
    assert new_queue.tail.val == 2


def test_enqueue_next(new_queue):
    """Test for enqueue affect node next poiner."""
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    assert new_queue.head.next_node.val == 3


def test_enqueue_prev(new_queue):
    """Test enqueue affect previous pointer."""
    new_queue.enqueue(2)
    new_queue.enqueue(3)
    assert new_queue.head.next_node.prev_node.val == 2


def test_multiple_enqueues(new_queue):
    """Test multiple enqueues affects head and tail."""
    new_queue.enqueue(2)
    new_queue.enqueue(4)
    assert new_queue.head.val == 2 and new_queue.tail.val == 4


def test_dequeue_returns_and_deletes_head(new_queue):
    """Test_dequeue_returns_and_deletes_head."""
    new_queue.enqueue(2)
    new_queue.enqueue(4)
    assert new_queue.dequeue() == 2


def test_dequeue_affects_next(new_queue):
    """Test dequeue affect next properly."""
    new_queue.enqueue(3)
    new_queue.enqueue(2)
    new_queue.enqueue(8)
    new_queue.dequeue()
    assert new_queue.head.next_node.val == 8


def test_peek_returns_head_val(new_queue):
    """Test_peek_returns_head.val."""
    new_queue.enqueue(3)
    new_queue.enqueue(4)
    assert new_queue.peek() == 3


def test_que_length(new_queue):
    """Test_que_length."""
    new_queue.enqueue(3)
    new_queue.enqueue(4)
    assert len(new_queue) == 2


def test_que_length_empty(new_queue):
    """Test_que_length."""
    assert len(new_queue) == 0


def test_que_size(new_queue):
    """Test_que_size."""
    new_queue.enqueue(3)
    new_queue.enqueue(4)
    assert new_queue.size() == 2


def test_que_size_empty(new_queue):
    """Test_que_size."""
    assert new_queue.size() == 0
