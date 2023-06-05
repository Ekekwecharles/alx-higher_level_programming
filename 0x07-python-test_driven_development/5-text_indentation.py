#!/usr/bin/python3
"""Text Indentation module"""


def text_indentation(text):
    """This function parses a text argument passed to it and prints two new
    lines anywhere it founds the characters '.', '?' and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""

    for char in text:
        new_text += char
        if char in ['.', '?', ':']:
            print(new_text.strip(' \t'))
            print()
            new_text = ""
        if char == '\n':
            print(new_text.strip(' \t'), end="")
            new_text = ""
    if new_text:
        print(new_text.strip(' \t'), end="")
