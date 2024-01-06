#!/usr/bin/env python3
"""return values with the appropriate types"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None


# Manually setting the annotations to display Optional as desired
    # if not Optional will print out typing.Union
safe_first_element.__annotations__ = {
    'lst': 'typing.Sequence[typing.Any]',
    'return': 'typing.Optional[typing.Any]'
}
