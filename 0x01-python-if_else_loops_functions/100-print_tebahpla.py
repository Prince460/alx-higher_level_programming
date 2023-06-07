#!/usr/bin/python3
# 100-print_tebahpla.py

""""Expected to print the alphabet in
reverse order alternating upper- and lower-case."""

h = 0

for c in range(ord('z'), ord('a') - 1, -1):

    print("{}".format(chr(c - h)), end="")

    h = 32 if h == 0 else 0
