from abc import abstractmethod
from typing import Protocol, final

from utils import cyan_print, sep_print


class TemplateMethod[A, B](Protocol):
    @abstractmethod
    def step_a(self) -> A: ...
    @abstractmethod
    def step_b(self) -> B: ...

    @final
    def run(self) -> tuple[A, B]:
        result_a = self.step_a()
        result_b = self.step_b()

        return (result_a, result_b)


class MakePair[T](TemplateMethod[T, T]):
    def __init__(self, a: T, b: T) -> None:
        self.a = a
        self.b = b

    def step_a(self) -> T:
        return self.a

    def step_b(self) -> T:
        return self.b


if __name__ == "__main__":
    sep_print()

    pair_maker = MakePair("Joaozinho", "Pedrinho")
    pair = pair_maker.run()
    cyan_print(pair, f"{pair[0]} {pair[1]}")
    sep_print()


    pair_maker = MakePair[tuple[int, int]]((1, 2), (3, 4))
    pair_a, pair_b = pair_maker.run()
    cyan_print(pair_a, pair_b, sum(pair_a + pair_b))
