
from abc import ABC, abstractmethod

from utils import cyan_print, sep_print


class Shape(ABC):
    @property
    @abstractmethod
    def area(self) -> int: ...

class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height

    @property
    def area(self) -> int:
        return self.width * self.height

class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side: int = side

    @property
    def area(self) -> int:
        return self.side * self.side

def use_rectangle(r: Rectangle) -> None:
    r.width = 5
    r.height = 4

    cyan_print(f"{type(r).__name__}", r.width, r.height, r.area)

    assert r.area == 20, "Área incorreta..."

if __name__ == "__main__":
    rectangle = Rectangle(50, 40)
    square = Square(10)

    sep_print()

    use_rectangle(rectangle)
    use_rectangle(square)

    sep_print()
