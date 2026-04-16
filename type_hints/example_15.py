
from collections.abc import Iterable, Sequence

from utils import cyan_print, sep_print


def filter_by_type[T](items: Iterable[object], type_: type[T]) -> list[T]:
    return [item for item in items if isinstance(item, type_)]

def reverse_in_groups[T](items: Sequence[T], group_size: int = 2) -> list[T]:
    return [
        group
        for index in range(0, len(items), group_size)
        for group in reversed(items[index:index + group_size])
    ]

if __name__ == "__main__":
    sep_print()

    mixed = [1, 2, 3, "a", "b", "c", {10, 20}]
    filtered: list[set[int]] = filter_by_type(mixed, set)
    cyan_print(filtered)

    reversed_groups = reverse_in_groups(mixed, group_size=4)
    cyan_print(reversed_groups)

    sep_print()
