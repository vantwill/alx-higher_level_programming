#!/usr/bin/python3
# 10-best_score.py
def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for t, g in a_dictionary.items():
        if g > big:
            big = g
            ret = t
    return (ret)
