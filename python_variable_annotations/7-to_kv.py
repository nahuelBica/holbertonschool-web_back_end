#!/usr/bin/env python3
"""
Convert key and value into a tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert  key and value into a tuple."""
    return (k, float(v**2))
