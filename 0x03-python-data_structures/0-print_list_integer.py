#!/usr/bin/python3
# 0-print_list_integer.py

def print_list_integer(my_list=[]):
    """Printing all the integers of a lists."""
    for u in range(len(my_list)):
        print("{:d}".format(my_list[u]))
