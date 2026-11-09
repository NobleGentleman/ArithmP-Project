import pytest

from arithmp.parser import Parser


def test_abs():
    assert Parser().parse("abs(-4)") == 4


def test_round():
    assert Parser().parse("round(2.6)") == 3


def test_two_arguments():
    assert Parser().parse("max(1, 5)") == 5


def test_unknown_function():
    with pytest.raises(NameError):
        Parser().parse("nope(1)")
