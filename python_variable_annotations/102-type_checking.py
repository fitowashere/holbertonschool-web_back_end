#!/usr/bin/env python3
"""return values with the appropriate types"""


from typing import Tuple, List


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
