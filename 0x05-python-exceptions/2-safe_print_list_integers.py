#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0
    len = 0
    while i < x:
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                len += 1
        except (ValueError, TypeError, IndexError):
            raise
        i += 1
    print()
    return len
