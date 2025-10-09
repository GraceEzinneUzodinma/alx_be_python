import math

class Shape:
    def area(self):
        return "NotImplementedError"
class Rectangle(Shape):
    def area(self, length, width):
        self.length = int(length)
        self.width = int(width)
        calculated_area = self.length * self.width
        return f"The area of the Rectangle is: {calculated_area}"
class Circle(Shape):
    def area(self, radius):
        self.radius = float(radius)
        calculated_area = math.pi * self.radius ** 2
        return f"The area of the Circle is: {calculated_area}"
shape = Rectangle()
print (shape.area(10, 5))
shape = Circle()
print(shape.area(7))
