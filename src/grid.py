

def if_zero(matrix):

    for midx, row in enumerate(matrix):
        for idx, val in enumerate(row):
            if val == 0:
                change_to_zero(matrix, idx)
                for idx in matrix[midx]:
                    matrix[midx][idx] = 0

    return matrix


def change_to_zero(matrix, idx):

    for row in matrix:
        row[idx] = 0


def test_if_zer0():
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [1, 5, 0, 7, 33],
        [6, 7, 8, 9, 10],
        [6, 7, 8, 9, 10],
    ]
    if_zero(matrix)
