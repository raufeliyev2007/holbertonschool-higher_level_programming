#!/usr/bin/python3
def delete_at(my_list1=[], idx=0):
    if idx < 0 or idx >= len(my_list1):
        return my_list1[:]
    new_list = []
    for i in range(len(my_list1)):
        if i != idx:
            new_list.append(my_list1[i])
    global my_list
    my_list = new_list
    return new_list
