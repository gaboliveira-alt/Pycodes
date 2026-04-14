
from collections.abc import Iterable

from utils import cyan_print, sep_print  # pyright: ignore[reportMissingTypeStubs]


def concatenation(items: Iterable[str]) -> str:
    return " ".join(items)


letters_list = ["a", "b", "c"]
letters_str = "abc"
letters_set = {"a", "b", "c"}
letters_tuple = ("a", "b", "c")
letters_dict = {"a": None, "b": False, "c": 123}

sep_print()

cyan_print(f"{concatenation(letters_list) =!r}")
cyan_print(f"{concatenation(letters_str) =!r}")
cyan_print(f"{concatenation(letters_set) =!r}")
cyan_print(f"{concatenation(letters_tuple) =!r}")
cyan_print(f"{concatenation(letters_dict) =!r}")
