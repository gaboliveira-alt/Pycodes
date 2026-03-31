from collections.abc import Callable

from utils import cyan_print, sep_print

sep_print()

def with_callback(
    x: float,
    y: float,
    callback: Callable[[str, str, bool], None]
    ) -> float:
        result = x + y
        callback(f"{result=}", "Another Value", True)
        return result

def callback(text: str, another_text: str, example_bool: bool = False) -> None:
    cyan_print(text, another_text, example_bool)

with_callback(2, 5, callback)
sep_print()


def with_args(*args: str) -> None:
    cyan_print(*args)

with_args("with_args", "a", "b", "c")
sep_print()


def with_kwargs(*args: int, **kwargs: str) -> None:
    cyan_print("Args:", *args)
    cyan_print("Kwargs", kwargs)

with_kwargs(1, 2, 3, example_name="Gabriel", age="19")
sep_print()
