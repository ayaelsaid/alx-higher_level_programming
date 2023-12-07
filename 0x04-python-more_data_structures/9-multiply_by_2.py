#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newa_dic = {}
    for key in a_dictionary.keys():
        value = a_dictionary[key]
        newa_dic[key] = value * 2
    return newa_dic
