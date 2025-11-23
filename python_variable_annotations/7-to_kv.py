#!/usr/bin/env python3
"""
Convert key and value into a tuple
"""
from typing import Tuple, Union


def to_kv(key: str, value: Union[int, float]) -> Tuple[str, float]:
    """Convert  key and value into a tuple."""
    return (key, float(value**2))
