from collections.abc import Callable
from typing import Protocol

from utils import cyan_print, sep_print

type ReallyRelaxedCallabe = Callable[..., None]
type MysticCallabe = Callable[[int, int, str], bool]


class CallbackProtocol(Protocol):
    def __call__(self, *, whatever: str) -> str: ...


def good_func(*, whatever: str) -> str:
    return whatever


def bad_func(*, not_good: str) -> str:
    return not_good

if __name__ == "__main__":
    sep_print()

    good: CallbackProtocol = good_func
    bad: CallbackProtocol = bad_func

    same_str_good = good(whatever="Bora bill")
    same_str_bad = bad(not_good="Aqui está sua string de volta")

    cyan_print(same_str_good)
    cyan_print(same_str_bad)

    sep_print()
