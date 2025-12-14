"""
is_none — tiny utility to check whether a value is exactly None.

Package on PyPI: "is-none"
Module import name: "is_none"

Goals:
- Extremely small, trivial, deterministic behavior: `x is None`.
- Type hints, tests, and a clear API for enterprises.
"""

from __future__ import annotations

from .is_none import is_none
from ._version_ import __version__

__all__ = ["is_none", "__version__"]
