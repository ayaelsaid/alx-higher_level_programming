#!/usr/bin/python3


def add_integer(a, b=98):
    """
    sum of nymbers
    Args:
        a: int or interger
        b: int or integer
    Retern:
        a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(a, float):
        b = int(b)
    return (a + b)
