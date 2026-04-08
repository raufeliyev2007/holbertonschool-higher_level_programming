#!/usr/bin/python3
def max_integer(my_list=[]):
    """Return the maximum integer in a list, or None if the list is empty."""
    if len(my_list) == 0:
        return None
    max_element = my_list[0]
    for i in my_list:
        if i > max_element:
            max_element = i
    return max_element
