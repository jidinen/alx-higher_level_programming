#!/usr/bin/python3


def replace_in_list(my_list: list, idx: int, element: int) -> list:

    """ replace and element at certain index"""
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
