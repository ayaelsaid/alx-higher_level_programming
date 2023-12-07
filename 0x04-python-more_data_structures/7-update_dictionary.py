#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    items = list(a_dictionary.keys())
    if key in items:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
