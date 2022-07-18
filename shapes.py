

class Rectangle:

    def __init__(self):
        length = 0
        width = 0

    def area(self):
        area = length * width
        return area

    def perimeter(self):
        perimeter = (2*length) + (2*width)
        return perimeter


class Square:
    def __init__(self):
        self.square = Rectangle()
