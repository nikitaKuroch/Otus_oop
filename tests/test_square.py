from src.Circle import Circle
from src.Square import Square
import pytest


@pytest.mark.parametrize("input_side, exp", [
    (4, 16),
    (7, 49),
    (0, "raise ValueError"),
    (-1, "raise ValueError")
])
def test_area(input_side, exp):
    square = Square(input_side)
    assert square.area == exp


@pytest.mark.parametrize("input_side, exp", [
    (5, 20),
    (3, 12),
    (0, "raise ValueError"),
    (-1, "raise ValueError")
])
def test_perimeter(input_side, exp):
    square = Square(input_side)
    assert square.perimeter == exp


@pytest.mark.parametrize("input, input2, exp", [
    (2, 2, 16),
    (1, 1, 4),
    (0, 2, "raise ValueError"),
    (-1, 2, "raise ValueError")
])
def test_add_area_1(input, input2, exp):
    square = Square(input)
    circle = Circle(input2)
    assert square.add_area(figure_2=circle) == exp
