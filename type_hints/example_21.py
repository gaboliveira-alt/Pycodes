from dataclasses import dataclass
from typing import Protocol

from utils import cyan_print, sep_print


class SupportsTalks(Protocol):
    name: str

    def talk(self, phrase: str) -> None: ...


@dataclass
class Person:
    name: str

    def talk(self, phrase: str) -> None:
        cyan_print(phrase)


@dataclass
class Toy:
    name: str

    def talk(self, phrase: str) -> None:
        cyan_print(phrase)


def talk(obj: SupportsTalks, phrase: str) -> None:
    cyan_print(f"{obj.__class__.__name__}{obj.name} will talk")
    obj.talk(phrase)


if __name__ == "__main__":
    sep_print()

    person1 = Person("Luiz")
    toy1 = Toy("Samsung")
    # supports_talk = SupportsTalk()  # cannot instantiate Protocol class...

    talk(person1, "I know how to talk.")
    talk(toy1, "I know how to talk.")

    sep_print()
