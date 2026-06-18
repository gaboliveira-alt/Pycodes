import inspect
from abc import ABC, abstractmethod
from collections.abc import Callable
from functools import wraps
from typing import Annotated, get_args, get_type_hints

from utils import cyan_print, sep_print  # type: ignore

s = sep_print
p = cyan_print


def validate_annotated[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    hints = get_type_hints(func, include_extras=True)

    signature = inspect.signature(func)

    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        bound_arguments = signature.bind(*args, **kwargs)
        bound_arguments.apply_defaults()

        if not hints:
            return func(*args, **kwargs)


        for arg_name in bound_arguments.arguments:
            if arg_name not in hints:
                continue

            value = bound_arguments.arguments[arg_name]
            metadata = get_args(hints[arg_name])

            if len(metadata) <= 1:
                continue

            type_, *validators = metadata

            for validator in validators:
                if not isinstance(validator, Validator):
                    continue

                if not isinstance(value, type_):
                    msg = (
                        f"Argument {arg_name!r} should be of type {type_!r} "
                        f"in {func.__name__!r}. Got {type(value)!r}."
                    )
                    raise TypeError(msg)
                validator.validate(value)
        return func(*args, **kwargs)
    return wrapper


class ValidationError(Exception):
    ...


class Validator[T](ABC):
    @abstractmethod
    def validate(self, value: T) -> T:
        ...


class IntRange(Validator[int]):
    def __init__(self, min_: int, max_: int) -> None:
        self.min_ = min_
        self.max_ = max_

    def validate(self, value: int) -> int:
        if value < self.min_ or value > self.max_:
            msg = f"{value} is out of range ({self.min_}, {self.max_})"
            raise ValidationError(msg)
        return value


class StrMaxLenght(Validator[str]):
    def __init__(self, max_: int) -> None:
        self.max_ = max_

    @validate_annotated
    def validate(self, value: str) -> str:
        if len(value) > self.max_:
            msg = f"{value!r} has more than {self.max_} characters"
            raise ValidationError(msg)
        return value


@validate_annotated
def set_height(height: Annotated[int, IntRange(1, 100)]) -> int:
    p(f"Height is set to {height}")
    return height


@validate_annotated
def set_app_name(
    name: Annotated[str, StrMaxLenght(10)]
) -> str:
    p(f"App name is now {name!r}")
    return name


if __name__ == "__main__":
    new_app_name = set_app_name(name="My App")
    new_height = set_height(height=1)
