#!/usr/bin/python3
import sys
if __name__ != "__main__":
    exit()
if len(sys.argv) == 1:
    print("0 arguments.")
elif len(sys.argv) == 2:
    print("{} argument:\n{}: {}".format(len(sys.argv) - 1, 1, sys.argv[1]))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
    index = 0
    for args in sys.argv[1:]:
        print("{}: {}".format(index + 1, args))
        index += 1
