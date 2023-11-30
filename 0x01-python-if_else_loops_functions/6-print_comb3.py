#!/usr/bin/python3
for i in range(10):
    for y in range(i + 1, 10):
        if i < 8 or y < 9:
            print("{:d}".format(i), end="")
            print("{:d},".format(y), end=" ")
        else:
            print("{:d}{:d}".format(i, y))
