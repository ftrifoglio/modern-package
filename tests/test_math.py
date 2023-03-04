from package.math import add, exponentiate, multiply, subtract


def test_add() -> None:
    assert add(1, 2) == 3


def test_subtract() -> None:
    assert subtract(1, 2) == -1


def test_multiply() -> None:
    assert multiply(1, 2) == 2


def test_exponentiate() -> None:
    assert exponentiate(2, 3) == 8
