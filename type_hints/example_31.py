from typing import TypedDict

from utils import cyan_print, sep_print


class Colored(TypedDict):
    background: str
    foreground: str


class Sized(TypedDict):
    width: int
    height: int


class Rectangle(Colored, Sized): ...


if __name__ == "__main__":
    sep_print()

    rectangle: Rectangle = {
        "background": "black",
        "foreground": "white",
        "width": 5,
        "height": 5,
    }


    cyan_print(rectangle["background"])
    cyan_print(rectangle["foreground"])
    cyan_print(rectangle["width"])
    cyan_print(rectangle["height"])

    sep_print()
