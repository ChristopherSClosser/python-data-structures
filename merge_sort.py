"""Implement merge sort."""


def merge_sort(items):
    """Return sorted list list."""
    mid = len(items) // 2
    left, right = items[:mid], items[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    sorted_items = []
    while left and right:
        if left[-1] >= right[-1]:
            sorted_items.insert(0, left.pop())
        else:
            sorted_items.insert(0, right.pop())
    return list(left or right) + sorted_items


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    from random import randint

    setup = 'from merge_sort import merge_sort'

    print('>>> best')
    for length in range(5, 20, 5):
        i = sorted([randint(-100, 100) for _ in range(length)])

        print('Input: {}'.format(len(i)))
        time = timeit('merge_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))

    print('=== average')
    for length in range(5, 20, 5):
        i = [randint(-100, 100) for _ in range(length)]

        print('Input: {}'.format(len(i)))
        time = timeit('merge_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))

    print('<<< worst')
    for length in range(5, 20, 5):
        i = sorted([randint(-100, 100) for _ in range(length)], reverse=True)

        print('Input: {}'.format(len(i)))
        time = timeit('merge_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))
