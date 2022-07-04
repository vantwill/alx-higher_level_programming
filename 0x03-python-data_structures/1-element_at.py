#!/usr/bin/python3
# 2-replace_in_list.py
def replace_in_list(my_list, indx, element):
    """Replace an element of a list at a specific position."""
    if indx >= 0 and indx < len(my_list):
        my_list[indx] = element
    return (my_list)
