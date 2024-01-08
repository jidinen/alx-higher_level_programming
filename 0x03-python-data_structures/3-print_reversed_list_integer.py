#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):

    """reverses a list"""
    if isinstance(my_list, list):
        lex = len(my_list)
        for i in range(lex - 1, -1, -1):
            print("{:d}".format(my_list[i]))
