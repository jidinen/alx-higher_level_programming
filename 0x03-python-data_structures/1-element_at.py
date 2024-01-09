#!/usr/bin/python3


def element_at(my_list: list, idx: int) -> int:

    """ deletes an element from a list"""
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]
