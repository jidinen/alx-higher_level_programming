#!/usr/bin/python3


def element_at(my_list, idx):

    """ deletes an element from a list"""
    if idx < 0:
        return (None)
    elif idx > len(my_list):
        return (None)
    mox = my_list[idx]
    return (mox)
