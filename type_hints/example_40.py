from collections.abc import Callable
from functools import wraps

from utils import cyan_print, sep_print


def simple_decorator_bad[R](func: Callable[..., R]) -> Callable[..., R]:
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> R:
        return func(*args, **kwargs)
    return wrapper


def simple_decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        cyan_print(f"{func.__name__!r} will be executed")

        result = func(*args, **kwargs)

        cyan_print(f"{func.__name__!r} was be executed")

        return result
    return wrapper


@simple_decorator
def add(x: int, y: int, /) -> int:
    return x + y


@simple_decorator
def keyword_only(*, value: str) -> str:
    return value

if __name__ == "__main__":
    sep_print()

    add_result = add(1, 2)
    cyan_print(f"{add_result = }")

    keyword_result = keyword_only(value="WOWWWW")
    cyan_print(f"{add_result = }")
