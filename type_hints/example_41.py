import inspect
from collections.abc import Callable
from functools import wraps

from utils import cyan_print, sep_print

type D[**P, R] = Callable[[Callable[P, R]], Callable[P, R]]
type Types = type | tuple[type, ...]


def valid_types[**P, R](**types: Types) -> D[P, R]:
    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        func_sig = inspect.signature(func)

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            bound_args = func_sig.bind(*args, **kwargs).arguments

            for param, arg in bound_args.items():
                if param not in types:
                    continue

                type_ = types[param]
                if isinstance(type_, tuple):
                    type_name = ", ".join([f"{t.__name__!r}" for t in type_])
                    type_name = " or ".join([f"{t.__name__!r}" for t in type_])
                else:
                    type_name = type_.__name__

                if not isinstance(arg, types[param]):
                    msg = f"{param!r} must be of type{type_name}"
                    raise TypeError(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@valid_types(x=int, y=(int, float))
def add(x: int, y: int, /) -> int:
    return x + y

@valid_types(value=str)
def keywords_only(*, value: str) -> str:
    return value

@valid_types(x=int, y=int, whatever=str, value=(str,))
def mixed(x: int, y: int, /, whatever: str, *, value: str) -> str:
    return f"{x=!r} {y=!r} {whatever=!r} {value=!r}"


if __name__ == "__main__":
    sep_print()

    add_result = add(12, 14)
    cyan_print(f"{add_result=!r}")


    keyword_result = keywords_only(value="minha mente meu coração")
    cyan_print(f"{keyword_result=!r}")


    mixed_result = mixed(1, 2, "abc", value="bora")
    cyan_print(f"{mixed_result=!r}")
