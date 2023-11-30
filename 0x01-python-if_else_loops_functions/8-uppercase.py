#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for c in str:
        if 'a' <= c <= 'z':
            str_upper += chr(ord(c) - ord('a') + ord('A'))
        else:
            str_upper += c
    print("{:s}".format(str_upper, end=""))
