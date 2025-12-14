from __future__ import annotations

from typing import Any


def is_none(value: Any) -> bool:
    """
    Determine whether a value is exactly `None`.

    Design Principles
    -----------------
    - Explicit over implicit
    - Deterministic behavior
    - Zero side effects
    - No dependency on truthiness or magic methods

    This function intentionally does not consider other falsy values
    (e.g. ``0``, ``""``, ``False``, ``[]``) to be None.

    Parameters
    ----------
    value : Any
        The value to evaluate.

    Returns
    -------
    bool
        ``True`` if and only if ``value is None``.

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
