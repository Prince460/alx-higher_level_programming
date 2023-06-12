#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    """Removing all characters c and C from a string."""
    copy = [r for r in my_string if r != 'c' and r != 'C']
    return ("".join(copy))
