import simple_math as sm
import pytest


@pytest.mark.parametrize("a, b, expected", [
    (0, 1, 1),
    (10, 2, 12),
    (-3, 5, 2)
])
def test_add(a, b, expected):
    assert sm.simple_add(a,b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (0, 1, -1),
    (10, 2, 8),
    (-3, 5, -8)
])
def test_sub(a, b, expected):
    assert sm.simple_sub(a,b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (0, 1, 0),
    (10, 2, 20),
    (-3, 5, -15)
])
def test_mult(a, b, expected):
    assert sm.simple_mult(a,b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (0, 1, 0),
    (10, 2, 5),
    (-10, 5, -2)
])
def test_div(a, b, expected):
    assert sm.simple_div(a,b) == expected




@pytest.mark.parametrize("x, a0, a1, expected", [
    (0, 1, 0, 1),
    (1, 1, 0, 1),
    (1, 1, 1, 2),
    (2, 1, 1, 3),
])
def test_poly_first(x, a0, a1, expected):
    assert sm.poly_first(x, a0, a1) == expected



@pytest.mark.parametrize("x, a0, a1, a2, expected", [
    (0, 1, 1, 1, 1),
    (1, 1, 1, 1, 3),
    (2, 1, 1, 1, 7),
    (3, 1, 1, 1, 13),
    (0, 4, 2, 1, 4),
    (1, 4, 2, 1, 7),
    (2, 4, 2, 1, 12),
    (3, 4, 2, 1, 19),

])
def test_poly_second(x, a0, a1, a2, expected):
    assert sm.poly_second(x, a0, a1, a2) == expected
