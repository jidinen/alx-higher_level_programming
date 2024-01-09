#!/usr/bin/python3


def element_at(my_list: list, idx: int) -> int:
    if idx < 0 or idx > len(my_list):
        return None
    """ return at certain index"""
    return my_list[idx]
