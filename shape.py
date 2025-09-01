"""Module defining Shape, Rectangle, and Circle classes."""
import math
#pylint: disable=too-few-public-methods
class Shape:
    """Base class for all shapes."""

    def __init__(self, color: str, name: str) -> None:
        """Initialize a Shape with a color and a name."""
        self.color = color
        self.name = name

    def say_name(self) -> str:
        """Return the name of the shape."""
        return f"My name is {self.name}."


class Rectangle(Shape):
    """Rectangle shape, subclass of Shape."""

    def __init__(self, color: str, name: str, width: float, height: float) -> None:
        """Initialize a Rectangle with width and height."""
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self) -> str:
        """Return the name of the rectangle."""
        return f"My name is {self.name} and I am a rectangle."

    def area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle shape, subclass of Shape."""

    def __init__(self, color: str, name: str, radius: float) -> None:
        """Initialize a Circle with a radius."""
        super().__init__(color, name)
        self.radius = radius

    def say_name(self) -> str:
        """Return the name of the circle."""
        return f"My name is {self.name} and I am a circle."

    def area(self) -> float:
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """Calculate and return the perimeter of the circle."""
        return 2 * math.pi * self.radius
