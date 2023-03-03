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
    args : int
        Numbers to subtract. Comma separated.

    Returns
    -------
    int
        Subtraction of all numbers.

    """
    return reduce(lambda a, b: a - b, list(nums))
