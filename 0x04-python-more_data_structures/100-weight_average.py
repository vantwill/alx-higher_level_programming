#!/usr/bin/python3
# 100-weight_average
def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    avgr = 0
    size = 0
    for tup in my_list:
        avgr += (tup[0] * tup[1])
        size += tup[1]
    return (avgr / size)
