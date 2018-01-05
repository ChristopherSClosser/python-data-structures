"""Test for Hash table."""
import pytest
import os
from hash_table import HashTable


@pytest.fixture(scope='session')
def eht():
    """Make an empty bst size of 10."""
    return HashTable(10)


@pytest.fixture(scope='session')
def wfile():
    """Read contents of dictionary."""
    path = '/usr/share/dict/words'
    with open(path, 'r') as doc:
        data = ' '.join([line.replace('\n', '') for line in doc.readlines(500)])
    return data.split(' ')


@pytest.fixture(scope='session')
def ht(wfile):
    """Make an empty bst size of 10."""
    ht = HashTable(10)
    for word in wfile:
        ht.set(word, word)
    return ht


def test_empty_hash_table(eht):
    """."""
    assert eht.size is 10


def test_entry_and_search(eht):
    """."""
    eht.set('turkey', 'turkey')
    assert eht.get('turkey') is 'turkey'


def test_entry_and_search_same_hash_dif_key(eht):
    """."""
    eht.set('keytur', 'turkey')
    eht.set('keyturx', 'giblets')
    assert eht.get('keyturx') == 'giblets'


def test_a_few_words(ht):
    """."""
    assert ht.get('Abernathy') == 'Abernathy'


def test_properly_handles_dup_keys(ht):
    """."""
    # key = ht.buckets[0].next.next.key
    # assert ht._hash(key) == 0


def test_last_entry(ht):
    """."""
    assert ht.get('Accra') == 'Accra'
