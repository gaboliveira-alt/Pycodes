from typing import NotRequired, TypedDict

from utils import cyan_print, sep_print

NiceDict = TypedDict(
    "NiceDict",
    {
        "first-name": str,
        "last-name": NotRequired[str],
        "birth-year": int,
        "in": NotRequired[bool],
        "__it-works": str | None,
    }
)


if __name__ == "__main__":
    sep_print()


    nice_dict: NiceDict = {
        "first-name": "Otávio",
        "last-name": "Miranda",
        "birth-year": 2000,
        "in": False,
        "__it-works": None,
    }


    cyan_print(nice_dict["first-name"])
    cyan_print(nice_dict["last-name"])

    sep_print()
