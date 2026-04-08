#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element at a given index in a list."""
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
