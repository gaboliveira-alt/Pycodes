from collections.abc import Callable


def identity_bad[R](func: Callable[..., R]) -> Callable[..., R]:
    return func


def add(x: float, y: float, /) -> float:
    return x + y


add_ = identity_bad(add)


def identity_good[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    return func


def multiply(x: float, y: float, /) -> float:
    return x * y


mult = identity_good(multiply)
