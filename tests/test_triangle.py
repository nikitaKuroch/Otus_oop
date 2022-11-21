from src.Triangle import Triangle
from src.Square import Square
import pytest


@pytest.mark.parametrize("input_side, exp", [
    ((4, 5, 3), 6),
    ((7, 6, 5), 14.696938456699069),
    ((1, 2, 2), 0.9682458365518543),
    ((2, 2, 111), "raise ValueError"),
    ((0, 0, 0), "raise ValueError"),
    ((-1, 5, 0), "raise ValueError"),
    ((2, 0, -1), "raise ValueError")
])
def test_area(input_side, exp):
    triangle = Triangle(a=input_side[0], b=input_side[1], c=input_side[2])
    assert triangle.area == exp


@pytest.mark.parametrize("input_side, exp", [
    ((4, 5, 3), 12),
    ((7, 6, 5), 18),
    ((1, 2, 2), 5),
    ((2, 2, 111), "raise ValueError"),
    ((0, 0, 0), "raise ValueError"),
    ((-1, 5, 0), "raise ValueError"),
    ((2, 0, -1), "raise ValueError")
])
def test_perimeter(input_side, exp):
    triangle = Triangle(a=input_side[0], b=input_side[1], c=input_side[2])
    assert triangle.perimeter == exp


@pytest.mark.parametrize("input, input2, exp", [
    (2, (2, 4, 5), 7.799671038392666),
    (5, (1, -2, 2), 'raise ValueError'),
    (5, (1, 2, -2), 'raise ValueError'),
    (5, (1, 0, 0), 'raise ValueError'),
    (5, (0, 2, 2), 'raise ValueError'),
    (1, (-1, 2, 2), "raise ValueError")
])
def test_add_area_3(input, input2, exp):
    square = Square(input)
    triangle = Triangle(a=input2[0], b=input2[1], c=input2[2])
    assert triangle.add_area(figure_2=square) == exp
