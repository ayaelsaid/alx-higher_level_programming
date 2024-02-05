#!/usr/bin/python3

def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    symbols = {".", "?", ":"}
    start_of_line = True

    for char in text:
        if char in symbols:
            print("{}\n\n".format(char, end=""))
            start_of_line = True
        else:
            if start_of_line and char.isspace():
                continue
            print(char, end="")
            start_of_line = False
