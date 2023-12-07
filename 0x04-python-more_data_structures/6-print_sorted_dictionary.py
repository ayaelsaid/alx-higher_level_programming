#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    items = list(a_dictionary.keys())
    items.sort()
    for key in items:
        value = a_dictionary[key]
        print("{:s}: {}".format(key, value))
