#!/usr/bin/env python3
"""return values with the appropriate types"""


from typing import Mapping, Any, TypeVar, Union


# Define a type variable
T = TypeVar
m = Mapping
u = Union
a = Any


def safely_get_value(dct: m, key: a, default: u[T, None] = None) -> u[a, T]:
    if key in dct:
        return dct[key]
    else:
        return default