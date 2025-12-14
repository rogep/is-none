import builtins
import math
import sys
import types

import pytest

from is_none import is_none


@pytest.mark.parametrize(
    "value, expected",
    [
        (None, True),
        (0, False),
        (False, False),
        ("", False),
        ([], False),
        ({}, False),
        (set(), False),
        (b"", False),
        (object(), False),
        (lambda: None, False),
    ],
)
def test_is_none_basic(value, expected):
    assert is_none(value) is expected


def test_is_none_identity_distinct_none_like_objects():
    # Different `None`-like constructs should NOT be treated as None.
    class Sentinel:
        def __bool__(self):
            return False

    sentinel = Sentinel()
    assert not is_none(sentinel)
    assert not is_none(0.0)
    assert not is_none(False)


def test_is_none_nan_and_float():
    # nan is not None
    assert not is_none(float("nan"))
    assert not is_none(math.nan)


def test_is_none_singleton_behaviour():
    # ensure exact identity comparison — create a dynamic None-like attribute
    # that is not None
    sentinel = object()
    assert not is_none(sentinel)


def test_is_none_types_and_modules():
    # type objects, modules etc are not None
    assert not is_none(int)
    assert not is_none(builtins)
    assert not is_none(sys)
    assert not is_none(types.ModuleType("fake_module"))


def test_is_none_typing_compat():

    assert not is_none(int | None)
