#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)[:2 - len(tuple_a)]
    tuple_b += (0, 0)[:2 - len(tuple_b)]

    i = tuple_a[0] + tuple_b[0]
    j = tuple_a[1] + tuple_b[1]

    return i, j
