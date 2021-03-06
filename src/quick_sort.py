"""Implement quick sorting algorithm.

Quicksort is a comparison sort, meaning that it can sort items of any type for
which a "less-than" relation (formally, a total order) is defined. In efficient
implementations it is not a stable sort, meaning that the relative order of
equal sort items is not preserved. Quicksort can operate in-place on an array,
requiring small additional amounts of memory to perform the sorting.
"""


def quick_sort(vals):
    """Return sorted list as copy."""
    if len(vals) <= 1:
        return vals[:]

    axis = vals[0]
    left = []
    right = []

    for val in vals[1:]:
        if val <= axis:
            left.append(val)
        else:
            right.append(val)

    return quick_sort(left) + [axis] + quick_sort(right)


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    from random import randint
    setup = 'from quick_sort import quick_sort'

    print('>>> best')
    for length in range(5, 20, 5):
        i = [randint(-100, 100) for _ in range(length)]

        print('Input: unsorted {}'.format(i))
        time = timeit('quick_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))

    print('<<< worst')
    for length in range(5, 20, 5):
        i = sorted([randint(-100, 100) for _ in range(length)])

        print('Input: sorted {}'.format(i))
        time = timeit('quick_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))
