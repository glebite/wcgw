"""badstring.py
"""
import string
import random

class BadString:
    """BadString
    """
    def __init__(self):
        self._internal = ""

    @property
    def internal(self):
        return self._internal

    @internal.setter
    def internal(self, value):
        self._internal = value

    @internal.deleter
    def internal(self):
        del self._internal
