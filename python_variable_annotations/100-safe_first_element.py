#!/usr/bin/env python3
"""return values with the appropriate types"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """return values with the appropriate types"""
    if lst:
        return lst[0]
    else:
        return None


