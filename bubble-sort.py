def bubble_sort(items):
    """Bubble sort function."""
    if isinstance(items, list):
        swaps = 1
        while swaps:
            swaps = 0
            for i in range(len(items) - 1):
                if items[i] > items[i + 1]:
                    items[i], items[i + 1] = items[i + 1], items[i]
                    swaps += 1
            if swaps == 0:
                return items
    else:
        raise TypeError('Function only accepts lists')


if __name__ == '__main__':  # pragma no cover
    import timeit as ti
    sort_1 = [1, 2, 4, 9, 10, 11]
    sort_2 = [17, 9, 7, 4, 1, 0]
    sort_3 = [random.randomint(0, 100) for i in range(6)]

    time_1 = ti.timeit("bubble_sort(sort_1)",
                       setup="from __main__ import sort_1, bubble_sort")
    time_2 = ti.timeit("bubble_sort(sort_2)",
                       setup="from __main__ import sort_2, bubble_sort")
    print("""
        Input: [1, 2, 4, 9, 10, 11]
        Good case: {}
        Input: [17, 9, 7, 4, 1, 0]
        Bad case: {}""".format(time_1, time_2))
        Input: {}
        Avg case: {}""".format(time_1, time_2)
