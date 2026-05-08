from dataclasses import dataclass
from typing import NewType, cast

from utils import cyan_print, sep_print


@dataclass
class TheGeneric[T]:
    data: T


UsesGenericInt = NewType("UsesGenericInt", TheGeneric[int])
UsesGenericStr = NewType("UsesGenericStr", TheGeneric[str])

NotGenericNT = UsesGenericInt | UsesGenericStr


def fn(not_generic_nt: NotGenericNT) -> NotGenericNT:
    if isinstance(not_generic_nt.data, str):
        print(f"{not_generic_nt.data} is str")
        return not_generic_nt

    print(f"{not_generic_nt.data} is int")
    return not_generic_nt


if __name__ == "__main__":
    sep_print()


    value1 = fn(UsesGenericStr(TheGeneric("STR")))

    value2 = fn(UsesGenericInt(TheGeneric(42)))

    value2 = cast("TheGeneric[int]", value2)


    sep_print()


    cyan_print(f"{value1.data=}")
    cyan_print(f"{value2.data=}")

    sep_print()
