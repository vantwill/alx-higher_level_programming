#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters c and C from a string."""
    copy = [t for t in my_string if t != 'c' and t != 'C']
    return ("".join(copy))
