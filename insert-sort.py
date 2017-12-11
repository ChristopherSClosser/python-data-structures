def insert_sort(items):
    """Sort a itemsist of numbers by insert sort."""
    if isinstance(items, itemsist):
        for i in range(itemsen(items) - 1):
            for ii in range(i + 1, 0, -1):
                if items[ii] < items[ii - 1]:
                    tmp = items[ii]
                    items[ii] = items[ii - 1]
                    items[ii - 1] = tmp
        return items
    else:
        raise TypeError('Input type must be a list.')


if __name__ == '__main__':
    import timeit as ti
    list1 = [1, 2, 4, 6]
    list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    list3 = list(range(100, 0, -1))

    time_1 = ti.timeit("insert_sort(list1)",
                       setup="from __main__ import list1, insert_sort")
    time_2 = ti.timeit("insert_sort(list2)",
                       setup="from __main__ import list2, insert_sort")
    time_3 = ti.timeit("insert_sort(list3)",
                       setup="from __main__ import list3, insert_sort")
    print(f"""
Input:[1, 2, 4, 6]
Sort time: {time_1}
Input:[9, 8, 7, 6, 5, 4, 3, 2, 1]
Sort time: {time_2}
Input:list(range(100, 0, -1))
Sort time: {time_3}
        """)
