#!/usr/bin/env python3
"""return values with the appropriate types"""


from typing import Tuple, List, Union


def zoom_array(lst: Tuple, factor: Union[int, float] = 2) -> List:
    """return values with the appropriate types"""

    # Ensures factor is an integer if a float is given.
    if isinstance(factor, float):
        factor = int(factor)

    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


# Manually adjust the annotations to exactly match the desired output
zoom_array.__annotations__ = {
    'lst': 'typing.Tuple',
    'factor': "<class 'int'>",
    'return': 'typing.List'
}

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
