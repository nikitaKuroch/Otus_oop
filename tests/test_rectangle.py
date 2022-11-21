from src.Rectangle import Rectangle
from src.Square import Square
import pytest


@pytest.mark.parametrize("input_side, exp", [
    ((4, 5), 20),
    ((7, 2), 14),
    ((0, 2), "raise ValueError"),
    ((2, 0), "raise ValueError"),
    ((0, 0), "raise ValueError"),
    ((-1, 5), "raise ValueError"),
    ((3, -1), "raise ValueError")
])
def test_area(input_side, exp):
    rectangle = Rectangle(side_a=input_side[0], side_b=input_side[1])
    assert rectangle.area == exp


@pytest.mark.parametrize("input_side, exp", [
    ((4, 5), 18),
    ((7, 5), 24),
    ((0, 2), "raise ValueError"),
    ((2, 0), "raise ValueError"),
    ((0, 0), "raise ValueError"),
    ((-1, 5), "raise ValueError"),
    ((3, -1), "raise ValueError")
])
def test_perimeter(input_side, exp):
    rectangle = Rectangle(side_a=input_side[0], side_b=input_side[1])
    assert rectangle.perimeter == exp


@pytest.mark.parametrize("input, input2, exp", [
    (2, (2, 4), 12),
    (2, (0, 2), 'raise ValueError'),
    (5, (-1, 0), "raise ValueError")
])
def test_add_area_2(input, input2, exp):
    square = Square(input)
    rectangle = Rectangle(side_a=input2[0], side_b=input2[1])
    assert rectangle.add_area(figure_2=square) == exp
