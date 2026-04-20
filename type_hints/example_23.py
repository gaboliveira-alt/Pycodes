from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

from utils import cyan_print, sep_print


class ShapeAbc(ABC):
    @property
    @abstractmethod
    def area(self) -> float: ...


@runtime_checkable
class ShapeProtocol(Protocol):
    @property
    def area(self) -> float: ...


class MyShapeAbc(ShapeAbc):
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @property
    def area(self) -> float:
        return self.x * self.y


class MyShapeProtocol:
    @property
    def area(self) -> float:
        return 1.1


def wants_shape_abc(shape: ShapeAbc) -> None:
    cyan_print(shape.area)


def wants_shape_protocol(shape: ShapeProtocol) -> None:
    cyan_print(shape.area)


if __name__ == "__main__":
    sep_print()


    myshape_abc = MyShapeAbc(10, 20)
    myshape_protocol = MyShapeProtocol()

    wants_shape_abc(myshape_abc)
    # wants_shape_abc(myshape_protocol)  # ❌ precisa herdar de ShapeAbc

    wants_shape_protocol(myshape_abc)  # ✅ bate por estrutura (tem .area -> float)
    wants_shape_protocol(myshape_protocol)  # ✅ idem

    sep_print()
