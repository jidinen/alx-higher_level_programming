#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    """a fuction that squares a 2X2 matrix"""
    result_list = []
    for x in matrix:
        new_list = list(map(lambda x: x * x, x))
        result_list.append(new_list)
    return result_list
