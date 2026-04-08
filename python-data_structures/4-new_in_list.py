#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list at a specific index
    without modifying the original list.
    """
    new_list = my_list.copy()  # make a copy of the original list
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
