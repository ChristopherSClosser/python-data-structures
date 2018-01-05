"""Implement instertion sort."""


def insertion_sort(vals):
    """Return sorted list."""
    s_l = vals[:]

    for i in range(len(s_l)):
        j = i
        while j > 0 and s_l[j] < s_l[j - 1]:
            s_l[j], s_l[j - 1] = s_l[j - 1], s_l[j]
            j -= 1

    return s_l


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    from random import randint

    setup = 'from insertion_sort import insertion_sort'

    print('>>> best')
    for length in range(5, 20, 5):
        i = sorted([randint(-100, 100) for _ in range(length)])

        print('Input: {}'.format(len(i)))
        time = timeit('insertion_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))

    print('=== average')
    for length in range(5, 20, 5):
        i = [randint(-100, 100) for _ in range(length)]

        print('Input: {}'.format(len(i)))
        time = timeit('insertion_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))

    print('<<< worst')
    for length in range(5, 20, 5):
        i = sorted([randint(-100, 100) for _ in range(length)], reverse=True)

        print('Input: {}'.format(len(i)))
        time = timeit('insertion_sort({})'.format(i), setup)
        print('    average time: {}ms\n'.format(time))
