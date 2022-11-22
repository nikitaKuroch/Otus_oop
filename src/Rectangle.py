from src.Figure import Figure


class Rectangle(Figure):
    NAME = "Rectangle"

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def perimeter(self):
        if self.side_a <= 0 or self.side_b <= 0:
            return "raise ValueError"
        else:
            return (self.side_b + self.side_a) * 2

    @property
    def area(self):
        if self.side_a <= 0 or self.side_b <= 0:
            return "raise ValueError"
        else:
            return self.side_b * self.side_a

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area
