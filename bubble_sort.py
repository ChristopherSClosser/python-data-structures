"""Implement bubble sort."""


def bubble_sort(items):
    """Bubble sort function."""
    swaps = 1
    while swaps:
        swaps = 0
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swaps += 1
        if swaps == 0:
            return items


if __name__ == '__main__':  # pragma no cover
    from timeit import timeit
    from random import randint

    setup = 'from bubble_sort import bubble_sort'

    print('>>> best')
    for length in range(5, 20, 5):
        i = sorted([randint(-100, 100) for _ in range(length)])

        print('Input: {}'.format(len(i)))
        time = timeit('bubble_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))

    print('=== average')
    for length in range(5, 20, 5):
        i = [randint(-100, 100) for _ in range(length)]

        print('Input: {}'.format(len(i)))
        time = timeit('bubble_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))

    print('<<< worst')
    for length in range(5, 20, 5):
        i = sorted([randint(-100, 100) for _ in range(length)], reverse=True)

        print('Input: {}'.format(len(i)))
        time = timeit('bubble_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))
