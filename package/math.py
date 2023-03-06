"""Math functions."""

from __future__ import annotations

from functools import reduce


def add(*nums: int | float) -> int | float:
    """
    Add all numbers.

    Parameters
    ----------
    nums : int or float
        Numbers to add. Comma separated.

    Returns
    -------
    int or float
        Sum of all numbers.

    """
    return reduce(lambda a, b: a + b, list(nums))


def subtract(*nums: int | float) -> int | float:
    """
    Subtract all numbers.

    Parameters
    ----------
    nums : int or float
        Numbers to subtract. Comma separated.

    Returns
    -------
    int or float
        Subtraction of all numbers.

    """
    return reduce(lambda a, b: a - b, list(nums))


def multiply(*nums: int | float) -> int | float:
    """
    Multiply all numbers.

    Parameters
    ----------
    nums : int or float
        Numbers to multiply. Comma separated.

    Returns
    -------
    int or float
        Multiplication of all numbers.

    """
    return reduce(lambda a, b: a * b, list(nums))


def exponentiate(base: int | float, exponent: int | float) -> int | float:
    """
    Calculate power of a number.

    Parameters
    ----------
    base : int or float
        Base number.
    exponent : int or float
        Exponent.

    Returns
    -------
    int or float
        Power of a number.

    """
    return base**exponent
