#!/usr/bin/python3
"""This Module returns a list of lists of integers representing
the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []

    p_triangles = [[1]]
    while len(p_triangles) != n:
        triangle = p_triangles[-1]
        temp = [1]
        for j in range(len(triangle) - 1):
            temp.append(triangle[j] + triangle[j + 1])
        temp.append(1)
        p_triangles.append(temp)
    return p_triangles
