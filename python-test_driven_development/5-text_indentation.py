#!/usr/bin/python3
"""
     Module for text_indentation functions


"""


def text_indentation(text):
    """ Text indentation function

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text is "":
        raise TypeError("text must be a string")

    newtext = ""
    delims = ".?:"
    space = " "

    for i in range(len(text)):
        if text[i] in space:
            if text[i-1] in delims:
                continue
        newtext += text[i]
        if text[i] in delims:
            newtext += "\n\n"
    print(newtext)
