#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.

    If idx is negative or out of range, returns a copy of the list unchanged.
    """
    # Return a copy if idx is invalid
    if idx < 0 or idx >= len(my_list):
        return my_list[:]

    # Build a new list excluding the element at idx
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    return new_list
