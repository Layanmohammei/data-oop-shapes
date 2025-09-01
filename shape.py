"""Module defining Shape, Rectangle, and Circle classes."""
import math

class Shape:
    """Base class for all shapes."""

    def __init__(self, color: str, name: str) -> None:
        self.color = color
        self.name = name

    def say_name(self) -> str:
        """Return the name of the shape."""
        return f"My name is {self.name}."


class Rectangle(Shape):
    """Rectangle shape, subclass of Shape."""

    def __init__(self, color: str, name: str, width: float, height: float) -> None:
        super().__init__(color, name)
        self.width = width
        self.height = height

    def say_name(self) -> str:
        return f"My name is {self.name} and I am a rectangle."

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle(Shape):
    """Circle shape, subclass of Shape."""

    def __init__(self, color: str, name: str, radius: float) -> None:
        super().__init__(color, name)
        self.radius = radius

    def say_name(self) -> str:
        return f"My name is {self.name} and I am a circle."

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
