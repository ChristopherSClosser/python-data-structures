"""Test trie."""

import pytest
import random
from trie_tree import Node, Trie


with open('/usr/share/dict/words') as f:
    FULL_LIST = [word.strip() for word in f]

TEST_WORDS = ['unwieldier', 'Quixote', 'illegalities', 'glands', 'pronoun',
              "bloodsucker's", 'jinni', 'belaying', 'Eve', 'dearly',
              'cloudier', 'tackle', "vein's", "multiplication's", 'entangles',
              "aftercare's", "literacy's", "childbearing's", 'Opal',
              'Inquisition', 'condescending', 'greying', "burden's", 'Lewis',
              'studying', 'sportscasts', 'explanatory', "minuteness's", 'Baku',
              'turbid', 'cogitation', "hairpin's", 'disappearances',
              "bathhouse's", 'delimiter', 'entrails', 'Chaplin', 'wigwagging',
              'hardiness', 'tome', 'humble', 'tubs', 'industrialist',
              "procrastinator's", "cornball's", "rubella's", 'Ngaliema',
              "now's", "Gatling's", 'mind']

TEST_WORDS = sorted(TEST_WORDS)


@pytest.fixture
def test_trie():
    """Create a small filled trie."""

    return Trie(TEST_WORDS)


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


def test_trie_has_star_root(trie):
    """."""
    assert trie.root.val == '*'


def test_trie_size(trie):
    """."""
    trie.insert('money')
    assert trie.size() == 1
    trie.insert('monkey')
    assert trie.size() == 2


def test_remove_for_non_string_raises_error(test_trie):
    """Test that remove for non-string raises a TypeError."""
    with pytest.raises(TypeError):
        test_trie.remove(1)


def test_remove_string_not_in_trie_raises_error(test_trie):
    """Test remove a word not in the trie raises a ValueError."""
    with pytest.raises(ValueError):
        test_trie.remove('chuck')


@pytest.mark.parametrize('num', [x for x in range(1, 10)])
def test_trie_has_words(num):
    """Test that trie has words."""
    words = random.sample(FULL_LIST, num)
    tree = Trie(words)
    assert tree._size == num


@pytest.mark.parametrize('test_trie, word', [(test_trie(), 'Ngaliema'),
                                             (test_trie(), 'hardiness'),
                                             (test_trie(), 'entangles'),
                                             (test_trie(), 'illegalities'),
                                             (test_trie(), 'Inquisition')])
def test_contains_returns_true_for_word_in_trie(test_trie, word):
    """Test contains(word) in the trie returns True."""
    assert test_trie.contains(word) is True


def test_remove_only_word_is_empty(trie):
    """Test that removing the only string from a trie empties it."""
    tree = trie
    tree.insert('chuck')
    tree.remove('chuck')
    assert tree.root.children == {}
    assert tree.size() == 0


@pytest.mark.parametrize('test_trie, word', [(test_trie(), 'Ngaliema'),
                                             (test_trie(), 'hardiness'),
                                             (test_trie(), 'entangles'),
                                             (test_trie(), 'illegalities'),
                                             (test_trie(), 'Inquisition'),
                                             (test_trie(), 'cloudier'),
                                             (test_trie(), 'Quixote'),
                                             (test_trie(), 'condescending'),
                                             (test_trie(), 'wigwagging'),
                                             (test_trie(), 'disappearances'),
                                             (test_trie(), 'Chaplin'),
                                             (test_trie(), 'entangles')])
def test_remove_string_from_trie_removes_the_string(test_trie, word):
    """Test that removing a string removes it from the trie."""
    assert test_trie.contains(word) is True
    test_trie.remove(word)
    assert test_trie.contains(word) is False


def test_trie_traverse(trie):
    """."""
    trie.insert('ill')
    trie.insert('illegal')
    trie.insert('illegalities')
    trie.insert('intent')
    trie.insert('intention')
    trie.insert('illintent')
    trie.insert('illegality')

    tree = trie.traverse()
    tl = list(tree)
    tl = ''.join(tl)
    import pdb; pdb.set_trace()
    assert 'egalit' in tl


def test_auto_complete(test_trie):
    """Test auto complete."""
