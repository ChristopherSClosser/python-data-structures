"""Implement radix sorting.

Radix sort is a non-comparative integer sorting algorithm that sorts data with
integer keys by grouping keys by the individual digits which share the same
significant position and value. A positional notation is required, but because
integers can represent strings of characters (e.g., names or dates) and
specially formatted floating point numbers, radix sort is not limited to
integers.
"""


def radix_sort(vals):
    """Return sorted list as copy."""
    if len(vals) <= 1:
        return vals[:]

    digits = len(str(max(vals)))

    for power in range(digits):
        buckets = [[] for _ in range(10)]

        for val in vals:
            trunc_val = val % (10 ** (power + 1))
            idx = trunc_val // (10 ** power)
            buckets[idx].append(val)
        res = []

        for bucket in buckets:
            for val in bucket:
                res.append(val)

        vals = res
    return vals
