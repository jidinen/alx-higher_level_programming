#!/usr/bin/python3


def no_c(my_string):

    """ deletes c in all strings """
    new_string = ""
    for char in my_string:
        if char.lower() != 'c' or char.upper() != 'C':
            new_string += char
    return new_string
