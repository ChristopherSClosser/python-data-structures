"""Implement quick sorting algorithm."""


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
