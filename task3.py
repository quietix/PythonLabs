import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f"I'm {self.__class__.__name__} with square {self.square()} and area {self.area()}."


class Rectangle(Figure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def square(self):
        return self.a * self.b

    def area(self):
        return (self.a + self.b) * 2

    def __str__(self):
        return f"{super().__str__()}\nI have sides a = {self.a}, b = {self.b}."


class Circle(Figure):
    def __init__(self, R: float):
        self.R = R

    def square(self):
        return math.pi * self.R ** 2

    def area(self):
        return 2 * math.pi * self.R

    def __str__(self):
        return f"{super().__str__()}\nI have radius R = {self.R}."


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def square(self):
        p = self.area() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def area(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f"{super().__str__()}\nI have sides a = {self.a}, b = {self.b}, c = {self.c}."


if __name__ == "__main__":
    r = Rectangle(10, 5)
    print(r, end="\n\n")

    c = Circle(5)
    print(c, end="\n\n")

    t = Triangle(3, 4, 5)
    print(t, end="\n\n")
