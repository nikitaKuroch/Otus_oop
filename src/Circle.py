from src.Figure import Figure


class Circle(Figure):
    NAME = "Circle"

    def __init__(self, r):
        self.r = r

    @property
    def perimeter(self):
        if self.r <= 0:
            return "raise ValueError"
        else:
            return 6 * self.r

    @property
    def area(self):
        if self.r <= 0:
            return "raise ValueError"
        else:
            return 3 * self.r ** 2

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area
