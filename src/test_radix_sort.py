"""Tests for radix_sort."""

import pytest

import random

from radix_sort import radix_sort


@pytest.mark.parametrize('nums', [[random.randint(0, 10) for _ in range(y)]
                                  for y in range(0, 20)])
def test_radix_sort_nums_0_to_10(nums):
    """Test_radix_sort_nums_0_to_10."""
    assert radix_sort(nums) == sorted(nums)


@pytest.mark.parametrize('nums', [[random.randint(0, 100) for _ in range(y)]
                                  for y in range(0, 20)])
def test_radix_sort_of_ints_orders_correctly_0_to_100(nums):
    """Test that bubble sort sorts ints correctly."""
    assert radix_sort(nums) == sorted(nums)


def test_radix_sort_does_not_alter_original_list():
    """Test_radix_sort_does_not_alter_original_list."""
    t_l = [5, 2, 7, 4, 1]
    s_l = radix_sort(t_l)
    assert s_l is not t_l
