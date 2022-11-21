from src.Figure import Figure


class Square(Figure):
    NAME = "Square"

    def __init__(self, side):
        self.side = side

    @property
    def perimeter(self):
        if self.side <= 0:
            return "raise ValueError"
        else:
            return self.side * 4

    @property
    def area(self):
        if self.side <= 0:
            return "raise ValueError"
        else:
            return self.side * self.side

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area
