#!/usr/bin/env python3
"""
    Function that gets a list of floats and int and return its sum
"""
from typing import List, Union


def sum_mixed_list(numbers: List[Union[float, int]]) -> float:
    """
    Function

    Args:
        input_list (list[float, int]): list of floats and int

    Return:
        float: sum of items
    """
    return sum(numbers)
