from typing import List

import numpy as np


def get_i_j_minor(matrix: List[List[int or float]], i: int, j: int):
    """Returns matrix by deleting its i-th row and j-th column."""
    return [[x for k, x in enumerate(row) if k != j] for l, row in enumerate(matrix) if l != i]


def det(matrix: List[List[int or float]]):
    """
    Calculates matrix determinant using Laplace's method. Assumes that matrix is list of
    """
    n = len(matrix)
    if n < 2:
        raise ValueError('Matrix should be at least 2x2.')

    if n != len(matrix[0]):
        raise ValueError('Matrix should be square.')

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        i = 0
        return sum(((-1) ** (i + j)) * matrix[i][j] * det(get_i_j_minor(matrix, i, j))
                   for j in range(n))


if __name__ == "__main__":

    sample_matrix = [[-2, 2, -3],
                     [-1, 1, 3],
                     [2, 0, -1]]

    assert (det(sample_matrix) == 18)

    # check using numpy
    epsilon = 1e-3
    for i in range(100):
        print(f'\ncheck {i}:')
        matrix_size = np.random.randint(low=3, high=10)
        random_matrix = np.random.randint(low=-10, high=10, size=(matrix_size, matrix_size))
        print('\nrandom matrix')
        print(random_matrix)

        numpy_result = np.linalg.det(random_matrix)
        our_result = det(random_matrix.tolist())
        print(f'numpy result: {numpy_result: {0}}')
        print(f'our result: {our_result: {1}}')

        if min(numpy_result, our_result) != 0:
            assert abs(numpy_result - our_result) / min(numpy_result, our_result) < epsilon
        else:
            assert abs(numpy_result - our_result) < epsilon
