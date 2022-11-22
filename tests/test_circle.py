from src.Circle import Circle
from src.Square import Square
import pytest


@pytest.mark.parametrize("input_side, exp", [
    (4, 48),
    (7, 147),
    (0, "raise ValueError"),
    (-1, "raise ValueError")
])
def test_area(input_side, exp):
    circle = Circle(input_side)
    assert circle.area == exp


@pytest.mark.parametrize("input_side, exp", [
    (5, 30),
    (3, 18),
    (0, "raise ValueError"),
    (-1, "raise ValueError")
])
def test_perimeter(input_side, exp):
    circle = Circle(input_side)
    assert circle.perimeter == exp


@pytest.mark.parametrize("input, input2, exp", [
    (2, 2, 16),
    (1, 1, 4),
    (0, 2, "raise ValueError"),
    (-1, 2, "raise ValueError")
])
def test_add_area_1(input, input2, exp):
    circle = Circle(input)
    square = Square(input2)
    assert circle.add_area(figure_2=square) == exp
