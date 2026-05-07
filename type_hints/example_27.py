import re
from typing import Protocol

from utils import cyan_print, sep_print

RE_COMMA_SPACE = re.compile(r"\s*,\s*")


class TypeCaster[T, R](Protocol):
    def __call__(self, *, value: T) -> R: ...


def to_str(*, value: object) -> str:
    return str(value)


def str_to_list(*, value: str) -> list[str]:
    clean_value = RE_COMMA_SPACE.sub(value, ",")
    return [
        value.strip() for value in RE_COMMA_SPACE.split(clean_value)
        if value.strip()
        ]


def wrong_kw_name(text: str) -> str:
    return text


def run_type_caster[T, R](value: T, type_caster: TypeCaster[T, R]) -> R:
    return type_caster(value=value)


if __name__ == "__main__":
    value_to_str = run_type_caster([1, 2, 3], to_str)
    values_to_list_str = run_type_caster(
        ",,,,abc,,,def,Luiz Otávio, a, b,c ,,,",
        str_to_list
    )

    sep_print()


    cyan_print(f"{value_to_str = }")
    cyan_print(f"{values_to_list_str = }")
