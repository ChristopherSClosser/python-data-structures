"""Test Priorityq."""

from priorityq import Priorityq
import pytest
from que_ import Queue
import pdb


@pytest.fixture
def pq():
    """."""
    return Priorityq()


def test_append_different_priorities(pq):
    """Highest priority should be 10."""
    pq.insert(1, 2)
    pq.insert(0, 10)
    assert pq._priority[0].priority == 10


def test_append_different_priorities_2(pq):
    """Value at first position should be 0."""
    pq.insert(1, 2)
    pq.insert(0, 10)
    assert pq._priority[0].head.val == 0


def test_append_different_priorities_3(pq):
    """Highest priority should be 100."""
    pq.insert(1, 2)
    pq.insert(0, 10)
    pq.insert(40, 100)
    assert pq._priority[0].priority == 100


def test_peek_returns_propper_head(pq):
    """Peek should return value associated with highest priority."""
    pq.insert(1, 0)
    pq.insert(2, 1)
    pq.insert(13, 1)
    pq.insert(0, 10)
    pq.insert(12, 2)
    pq.insert(40, 2)
    assert pq.peek() == 0


def test_queue_has_priority():
    """Queue should have priority attribute."""
    q = Queue(3)
    assert q.priority == 3


def test_q_insert_1(pq):
    """Insert should set priority value of 1."""
    pq.insert(1, 1)
    assert pq._priority[0].priority == 1


def test_q_insert_2(pq):
    """Length of queue in position one should grow if same priorities."""
    pq.insert(1, 1)
    pq.insert(2, 1)
    assert len(pq._priority[0]) == 2


def test_q_insert_2_priorities(pq):
    """Length should be 2 since 2 different priorities added."""
    pq.insert(1, 1)
    pq.insert(2, 0)
    assert len(pq._priority) == 2


def test_q_insert_2nodes_1_priority_default(pq):
    """Test that default priority works."""
    pq.insert(1, 1)
    pq.insert(2)
    assert len(pq._priority) == 2


def test_q_insert_lower_priority(pq):
    """A lower priority than 0 should change self.lowest."""
    pq.insert(1, 1)
    pq.insert(1, -1)
    assert pq.lowest == -1


def test_queue_inserted_correct_order(pq):
    """10 should be the priority in the first position."""
    pq.insert(1, 1)
    pq.insert(1, 10)
    assert pq._priority[0].priority == 10


def test_queue_inserted_correct_order_2(pq):
    """Same as above but reversed order."""
    pq.insert(1, 10)
    pq.insert(1, 1)
    assert pq._priority[0].priority == 10


def test_peek_empty_priorityq(pq):
    """Peek returns none on empty priority queue."""
    assert pq.peek() is None


def test_peek_several_vals(pq):
    """Peek returns the value of highest priority."""
    pq.insert(1, 1)
    pq.insert(2, 5)
    assert pq.peek() == 2


def test_empty_priorityq_pop(pq):
    """Pop should cause error when called on empty pq."""
    with pytest.raises(IndexError):
        pq.pop()


def test_pq_pop(pq):
    """Pop should return the value of highest priority."""
    pq.insert(1, 1)
    pq.insert(2, 5)
    assert pq.pop() == 2


def test_list_pop_2(pq):
    """Pop should remove queue from list if queue becomes empty afetr pop."""
    pq.insert(1, 1)
    pq.insert(2, 5)
    pq.pop()
    # pdb.set_trace()
    assert len(pq._priority) == 1
