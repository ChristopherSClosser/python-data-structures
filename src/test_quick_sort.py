"""Test quick sort."""

import pytest

import random

from quick_sort import quick_sort


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


@pytest.mark.parametrize('nums', [[random.randint(-100, 100)
                                  for _ in range(y)]
                                  for y in range(0, 20)])
def test_quick_sort_orders_properly(nums):
    """Test_quick_sort_orders_properly."""
    assert quick_sort(nums) == sorted(nums)


@pytest.mark.parametrize('nums', [[random.uniform(-100, 100)
                                  for _ in range(y)]
                                  for y in range(0, 20)])
def test_quick_sort_with_floats(nums):
    """Test_quick_sort_with_floats."""
    assert quick_sort(nums) == sorted(nums)


@pytest.mark.parametrize('words', [random.sample(TEST_WORDS, y)
                                   for y in range(0, 20)])
def test_quick_sort_words(words):
    """Test quick sort works with words."""
    assert quick_sort(words) == sorted(words)


def test_quick_sort_does_not_mutate_the_original_list():
    """Test_quick_sort_does_not_mutate_the_original_list."""
    t_l = [5, 2, 7, 4, 1]
    s_l = quick_sort(t_l)
    assert s_l is not t_l
