#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for digitone in range(0, 10):
    for digittwo in range(digitone + 1, 10):
        if digitone == 8 and digittwo == 9:
            print("{}{}".format(digitone, digittwo))
        else:
            print("{}{}".format(digitone, digittwo), end=", ")
