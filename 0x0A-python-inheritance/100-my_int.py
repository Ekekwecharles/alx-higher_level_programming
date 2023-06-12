#!/usr/bin/python3
"""Module that inherits from the int class"""


class MyInt(int):
    """Inverts the result of eq and ne"""
    def __eq__(self, other):
        """Return iverted result"""
        return super().__ne__(other)
    
    def __ne__(self, other):
        """Return inverted result"""
        return super().__eq__(other)
