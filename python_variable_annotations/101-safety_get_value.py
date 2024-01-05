#!/usr/bin/env python3
"""return values with the appropriate types"""


from typing import Mapping, Any, TypeVar, Union


# Define a type variable
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
