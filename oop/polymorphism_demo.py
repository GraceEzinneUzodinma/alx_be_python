import math

class Shape:
    def __init__(self):
        pass
    def area(self):
        return "NotImplementedError"
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = int(length)
        self.width = int(width)
    def area(self):
        calculated_area = self.length * self.width
        return {calculated_area}
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = float(radius)
    def area(self):
        calculated_area = math.pi * self.radius ** 2
        return {calculated_area}