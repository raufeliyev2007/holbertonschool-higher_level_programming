#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns the key with the highest value in a dictionary."""
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    count = 0
    value = 0
    for key in a_dictionary:
        count += 1
        if a_dictionary[key] > value:
            value = a_dictionary[key]
    if count != 0:
        for key in a_dictionary:
            if a_dictionary[key] == value:
                return key
    else:
        return None
