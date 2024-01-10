#!/usr/bin/python3


def search_replace(my_list, search, replace):

    """search and replaces at certain index"""
    new_list = []
    for x in my_list:
        if x == search:
            new_list.append(replace)
        else:
            new_list.append(x)
    return new_list
