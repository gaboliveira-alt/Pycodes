import sys
from typing import Never, NoReturn

from utils import cyan_print, sep_print


def quit_program() -> NoReturn:
    sys.exit(0)


def no_return_func() -> NoReturn:
    raise RuntimeError


def never() -> Never:
    raise RuntimeError


def ask_user() -> Never:
    while True:
        input_user = input("Digite algo ai: ")
        exit_words = "q", "exit"

        if input_user.lower in exit_words:
            cyan_print("Bye")
            quit_program()
            print("Isso é impossivel")
        cyan_print(f"ECHO: {input_user}")
    cyan_print("Isso é impossivel tambem")


if __name__ == "__main__":
    sep_print()

    should_run = True

    if should_run:
        print("Seu script vai rodar normal")
    else:
        never()
        print("Isso é impossivel")

    sep_print()
