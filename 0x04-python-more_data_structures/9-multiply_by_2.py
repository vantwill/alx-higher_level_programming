#!/usr/bin/python3
# 9-multiple_by_2.py
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({t: a_dictionary[k] * 2 for t in a_dictionary})
