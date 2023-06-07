#!/usr/bin/python3
"""Matrix division module"""


def matrix_divided(matrix, div):
    """Divides each element of the 2 dimensional matrix"""
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not matrix or matrix == [] \
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')
    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
