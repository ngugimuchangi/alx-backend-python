#!/usr/bin/env python3
""" Complex annotation module:
    Mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ Function to add a list of floats and ints"""
    return sum(mxd_lst)
