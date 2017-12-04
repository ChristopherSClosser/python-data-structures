"""Test for Hash table."""
import pytest
from hash_table import HashTable


@pytest.fixture
def eHt():
    """Make an empty bst size of 10."""
    return HashTable(10)


def test_empty_hash_table(eht):
    """."""
    assert eht.size is 10
