from collections.abc import Sequence
from typing import TypeGuard, TypeIs, reveal_type

from utils import sep_print


def is_list_str_guard(values: Sequence[object]) -> TypeGuard[list[str]]:
    has_only_str = [isinstance(value, str) for value in values]
    return all(has_only_str)


def is_list_str_is(values: Sequence[object]) -> TypeIs[list[str]]:
    has_only_str = [isinstance(value, str) for value in values]
    return all(has_only_str)


if __name__ == "__main__":
    sep_print()

    items_guard = [22, "b"]

    if is_list_str_guard(items_guard):
        reveal_type(items_guard)
    else:
        reveal_type(items_guard)

    reveal_type(items_guard)

    sep_print()

    items_is = [22, "a"]

    if is_list_str_is(items_is):
        reveal_type(items_is)
    else:
        reveal_type(items_is)

    reveal_type(items_is)

    sep_print()
