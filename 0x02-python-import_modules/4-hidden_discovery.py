#!/usr/bin/python3
import hidden_4
if __name__ != "__main__":
    exit()

for name in dir(hidden_4):
    if name.startswith("__"):
        continue
    print("{}".format(name))
