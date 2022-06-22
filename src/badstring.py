"""badstring.py

Experiments of odds and ends.
"""
import string
import random

class BadString:
    """BadString
    """
    def __init__(self):
        self._internal = ""
        self._impairments = list()

    @property
    def internal(self):
        return self._internal

    @internal.setter
    def internal(self, value):
        self._internal = value

    @internal.deleter
    def internal(self):
        del self._internal

    @property
    def impairments(self):
        return self_impairments

    @impairments.setter
    def impairments(self, impairment_function):
        self._impairments.append(impairment_function)

    @impairments.deleter
    def impairments(self):
        del self._impairments

    
