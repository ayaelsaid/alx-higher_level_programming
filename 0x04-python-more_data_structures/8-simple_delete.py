#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    items = list(a_dictionary.keys())
    if key in items:
        a_dictionary.pop(key)
    return a_dictionary
