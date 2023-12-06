#!/usr/bin/python3
def uniq_add(my_list=[]):
    mynew_list = 0
    new_list = set(my_list)
    for item in new_list:
        mynew_list += item
    return mynew_list
