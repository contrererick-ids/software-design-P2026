from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def getPerimeter(self):
        pass

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        if isinstance(side1, (int, float)) and isinstance(side2, (int, float)) and isinstance(side3, (int, float)):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3

    def getPerimeter(self):
        if not hasattr(self, 'side1') or not hasattr(self, 'side2') or not hasattr(self, 'side3'):
            return "Cannot calculate perimeter due to invalid sides."
        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            return "Sides must be positive numbers."
        if self.side1 <= self.side2 + self.side3 and self.side2 <= self.side1 + self.side3 and self.side3 <= self.side1 + self.side2:
            return self.side1 + self.side2 + self.side3
        else:
            return "Invalid triangle sides."
    
    def getArea(self):
        if not hasattr(self, 'side1') or not hasattr(self, 'side2') or not hasattr(self, 'side3'):
            return "Cannot calculate area due to invalid sides."
        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            return "Sides must be positive numbers."
        if self.getPerimeter() == "Invalid triangle sides.":
            return "Cannot calculate area for invalid triangle."
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

class Rectangle(Figure):
    def __init__(self, length, width):
        if isinstance(length, (int, float)) and isinstance(width, (int, float)):
            self.length = length
            self.width = width

    def getPerimeter(self):
        if not hasattr(self, 'length') or not hasattr(self, 'width'):
            return "Cannot calculate perimeter due to invalid dimensions."
        if self.length <= 0 or self.width <= 0:
            return "Length and width must be positive numbers."
        return 2 * (self.length + self.width)
    
    def getArea(self):
        if not hasattr(self, 'length') or not hasattr(self, 'width'):
            return "Cannot calculate area due to invalid dimensions."
        if self.length <= 0 or self.width <= 0:
            return "Length and width must be positive numbers."
        return self.length * self.width

class Circle(Figure):
    def __init__(self, radius):
        if isinstance(radius, (int, float)):
            self.radius = radius
    
    def getPerimeter(self):
        if not hasattr(self, 'radius'):
            return "Cannot calculate perimeter due to invalid radius."
        if self.radius <= 0:
            return "Radius must be a positive number."
        return 2 * 3.1416 * self.radius
    
    def getArea(self):
        if not hasattr(self, 'radius'):
            return "Cannot calculate area due to invalid radius."
        if self.radius <= 0:
            return "Radius must be a positive number."
        return 3.1416 * (self.radius ** 2)

def test_triangle():
    print("==========================TRIANGLE CLASS TESTS==========================\n")
    print("=► Testing Triangle class with various inputs:\n")
    triangle_positive_numbers = Triangle(3, 4, 5)
    triangle_negative_numbers = Triangle(-3, -4, -5)
    triangle_zero = Triangle(0, 0, 0)
    triangle_letters = Triangle('a', 'b', 'c')
    triangle_null = Triangle(None, None, None)
    triangle_impossible = Triangle(1, 1, 100)

    lsit_of_triangles = [triangle_positive_numbers, triangle_negative_numbers, triangle_zero, triangle_letters, triangle_null, triangle_impossible]

    triangle_counter = 1
    for triangle in lsit_of_triangles:
        try:
            print(f"--- Triangle {triangle_counter} ---")
            print(f"• Sides: {getattr(triangle, 'side1', 'Invalid')}, {getattr(triangle, 'side2', 'Invalid')}, {getattr(triangle, 'side3', 'Invalid')}")
            print(f"• Perimeter of triangle {triangle_counter}: {triangle.getPerimeter()}")
            print(f"• Area of triangle {triangle_counter}: {triangle.getArea()}")
            triangle_counter += 1
        except Exception as e:
            print(f"Error processing triangle {triangle_counter}: {e}")
            triangle_counter += 1

def test_rectangle():
    print("\n==========================RECTANGLE CLASS TESTS==========================\n")
    print("=► Testing Rectangle class with various inputs:\n")
    rectangle_positive_numbers = Rectangle(4, 5)
    rectangle_negative_numbers = Rectangle(-4, -5)
    rectangle_zero = Rectangle(0, 0)
    rectangle_letters = Rectangle('a', 'b')
    rectangle_null = Rectangle(None, None)

    lsit_of_rectangles = [rectangle_positive_numbers, rectangle_negative_numbers, rectangle_zero, rectangle_letters, rectangle_null]

    rectangle_counter = 0
    for rectangle in lsit_of_rectangles:
        try:
            print(f"--- Rectangle {rectangle_counter} ---")
            print(f"• Length and Width: {getattr(rectangle, 'length', 'Invalid')}, {getattr(rectangle, 'width', 'Invalid')}")
            print(f"• Perimeter of rectangle {rectangle_counter}: {rectangle.getPerimeter()}")
            print(f"• Area of rectangle {rectangle_counter}: {rectangle.getArea()}")
            rectangle_counter += 1
        except Exception as e:
            print(f"Error processing rectangle {rectangle_counter}: {e}")
            rectangle_counter += 1

def test_circle():
    print("\n==========================CIRCLE CLASS TESTS==========================\n")
    print("=► Testing Circle class with various inputs:\n")
    circle_positive_number = Circle(5)
    circle_negative_number = Circle(-5)
    circle_zero = Circle(0)
    circle_letter = Circle('a')
    circle_null = Circle(None)

    lsit_of_circles = [circle_positive_number, circle_negative_number, circle_zero, circle_letter, circle_null]

    circle_counter = 0
    for circle in lsit_of_circles:
        try:
            print(f"--- Circle {circle_counter} ---")
            print(f"• Radius: {getattr(circle, 'radius', 'Invalid')}")
            print(f"• Perimeter of circle {circle_counter}: {circle.getPerimeter()}")
            print(f"• Area of circle {circle_counter}: {circle.getArea()}")
            circle_counter += 1
        except Exception as e:
            print(f"Error processing circle {circle_counter}: {e}")
            circle_counter += 1

def main():

    test_triangle()
    test_rectangle()
    test_circle()

main()