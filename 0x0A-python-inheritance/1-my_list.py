#!/usr/bin/python3
"""Module that inherits from the list class"""


class MyList(list):
    """Mylist Class"""
    def print_sorted(self):
        """Prints the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
