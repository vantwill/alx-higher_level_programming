#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    midl_e = size
    midl = size // 2

    if size == 0:
        return None

    while True:
        midl_e = mid_e // 2
        if (midl < size - 1 and
                list_of_integers[midl] < list_of_integers[midl + 1]):
            if midl_e // 2 == 0:
                midl_e = 2
            midl = midl + midl_e // 2
        elif midl_e > 0 and list_of_integers[midl] < list_of_integers[midl - 1]:
            if midl_e // 2 == 0:
                midl_e = 2
            midl = midl - midl_e // 2
        else:
            return list_of_integers[midl]
