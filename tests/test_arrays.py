from arithmp.parser import Parser


def test_array_literal():
    assert Parser().parse("{1, 2, 3}") == [1, 2, 3]


def test_empty_array():
    assert Parser().parse("{}") == []


def test_index():
    assert Parser().parse("{10, 20, 30}[1]") == 20


def test_index_with_expression():
    assert Parser().parse("{10, 20, 30}[1 + 1]") == 30
