#!/usr/bin/python3


def def multiply_list_map(my_list=[], number=0):

    """using map """
    new_list = list(map(lambda(n: n * number, my_list)))
    return new_list
