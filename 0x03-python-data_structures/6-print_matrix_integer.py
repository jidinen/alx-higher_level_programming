#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]) -> None:

    """print in matrix form"""
    for row in matrix:
        for column in row:
           print("{:d}".format(column), end=" " if column != row[-1] else "")
    print()
