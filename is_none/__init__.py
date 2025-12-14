"""
is_none — tiny utility to check whether a value is exactly None.

Package on PyPI: "is-none"
Module import name: "is_none"

Goals:
- Extremely small, trivial, deterministic behavior: `x is None`.
- Type hints, tests, and a clear API for enterprises.
"""

from __future__ import annotations

__all__ = ["is_none", "__version__"]
__version__ = "0.1.0"

from typing import Any


def is_none(value: Any) -> bool:
    """
    Return True if ``value`` is exactly ``None`` (identity comparison),
    otherwise return False.

    Rationale
    ---------
    Use identity comparison (`is`) because it's the only reliable
    test for the singleton None. This intentionally does not treat
    other "falsy" values (0, "", False, []) as None.

    Examples
    --------
    >>> is_none(None)
    True
    >>> is_none(0)
    False
    >>> is_none("")
    False
    """
    return value is None
