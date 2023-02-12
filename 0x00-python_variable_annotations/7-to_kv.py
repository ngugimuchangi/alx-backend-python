#!/usr/bin/env python3
""" Complex annotation type module:
    string and int/float to tuple
"""
from typing import List, Tuple, Union

int_float = Union[int, float]


def to_kv(k: str, v: int_float) -> Tuple[str, int_float]:
    """ Function to return a tuple of str and int or float
        based on passed arguments
    """
    return (k, (v * v))
