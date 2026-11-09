import pytest

from arithmp.parser import Parser

def test_assign_returns_value():
    assert Parser().parse("a = 4") == 4


def test_assign_then_use():
    p = Parser()
    p.parse("a = 4")
    assert p.parse("a + 1") == 5

def test_reassign():
    p = Parser()
    p.parse("a = 1")
    p.parse("a = a + 1")
    assert p.parse("a") == 2


def test_undefined_variable():
    with pytest.raises(NameError):
        Parser().parse("a + 1")
