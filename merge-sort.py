def merge_sort(items):
    """Sort itemsuence by merge sort."""
    if isinstance(items, list):
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
    else:
        raise TypeError('Input type must be a list.')


if __name__ == '__main__':
    import timeit as ti
    list1 = [1, 2, 4, 6]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    list3 = list(range(100, 0, -1))
    count = 100000

    time_1 = ti.timeit("merge_sort(list1[:])",
                       setup="from __main__ import list1, merge_sort",
                       number=count)
    time_2 = ti.timeit("merge_sort(list2[:])",
                       setup="from __main__ import list2, merge_sort",
                       number=count)
    time_3 = ti.timeit("merge_sort(list3[:])",
                       setup="from __main__ import list3, merge_sort",
                       number=count)
    print(f"""
Input:[1, 2, 4, 6]
Sort time: {time_1/count}
Input:[9, 8, 7, 6, 5, 4, 3, 2, 1]
Sort time: {time_2/count}
Input:list(range(100, 0, -1))
Sort time: {time_3/count}
        """)
