"""Math functions."""

from functools import reduce


def add(*nums: int) -> int:
    """
    Add all numbers.

    Parameters
    ----------
    nums : int
        Numbers to add. Comma separated.

    Returns
    -------
    int
        Sum of all numbers.

    """
    return reduce(lambda a, b: a + b, list(nums))


def subtract(*nums: int) -> int:
    """
    Subtract all numbers.

    Parameters
    ----------
    nums : int
        Numbers to subtract. Comma separated.

    Returns
    -------
    int
        Subtraction of all numbers.

    """
    return reduce(lambda a, b: a - b, list(nums))


def multiply(*nums: int) -> int:
    """
    Multiply all numbers.

    Parameters
    ----------
    nums : int
        Numbers to multiply. Comma separated.

    Returns
    -------
    int
        Multiplication of all numbers.

    """
    return reduce(lambda a, b: a * b, list(nums))


def exponentiate(base: int, exponent: int) -> int:
    """
    Calculate power of a number.

    Parameters
    ----------
    base : int
        Base number.
    exponent : int
        Exponent.

    Returns
    -------
    int
        Power of a number.

    """
    return base**exponent
